from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List, Optional
import random
import requests
from backend.config import API_URL, APP_DEFAULTS, format_time, needs_scrolling, format_song, format_search_results, get_download_url
from pathlib import Path

app = FastAPI(
    title="Music Player API",
    description="API untuk aplikasi Music Player",
    version="1.0.0",
    openapi_tags=[
        {
            "name": "Songs",
            "description": "Endpoint untuk mengelola lagu.",
        },
        {
            "name": "Player",
            "description": "Endpoint untuk mengelola pemutar musik.",
        },
    ],
)

# Konfigurasi CORS (Cross-Origin Resource Sharing)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Menambahkan middleware untuk file statis
app.mount("/static", StaticFiles(directory="."), name="static")

# Model Data
class Song(BaseModel):
    id: str
    title: str
    artist: str
    thumbnail: str
    videoUrl: str
    timestamp: Optional[str] = None

class DownloadResponse(BaseModel):
    data: Optional[dict] = None
    status: bool

# State Aplikasi
recently_played: List[Song] = [] # Menggunakan List[Song]
current_playlist: List[Song] = [] # Menggunakan List[Song]
current_song_index: int = 0
is_playing: bool = False
is_shuffle: bool = False
is_repeat: bool = False

# Endpoint API

@app.get("/", response_class=HTMLResponse)
async def read_root():
    """Menampilkan index.html ketika mengakses root."""
    index_path = Path("index.html")
    if not index_path.exists():
        raise HTTPException(status_code=404, detail="index.html not found")
    with open(index_path, "r", encoding="utf-8") as f:
        return f.read()

@app.get("/search", tags=["Songs"], description="Mencari lagu berdasarkan query.")
async def search_songs(query: str):
    try:
        response = requests.get(f"{API_URL['SEARCH']}?query={query}")
        response.raise_for_status()
        data = response.json()

        if not data.get("status") or not data.get("data") or len(data.get("data")) == 0:
            return JSONResponse(content={"status": False, "data": []})

        global current_playlist
        current_playlist = [Song(**item) for item in format_search_results(data["data"])] # Mengubah dictionary menjadi objek Song
        return JSONResponse(content={"status": True, "data": [song.dict() for song in current_playlist]}) # Mengubah objek Song menjadi dictionary sebelum dikirim
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error fetching search results: {e}")

@app.get("/download_mp3", response_model=DownloadResponse, tags=["Songs"], description="Mendapatkan URL unduhan MP3 dari URL video.")
async def download_mp3(url: str):
    try:
        response = requests.get(f"{API_URL['DOWNLOAD_MP3']}?url={url}")
        response.raise_for_status()
        data = response.json()
        return DownloadResponse(status=True, data=data.get("data"))
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error getting MP3 download URL: {e}")

@app.get("/play/{index}", tags=["Player"], description="Memutar lagu berdasarkan indeks dalam playlist.")
async def play_song(index: int):
    global current_song_index, is_playing
    if index < 0 or index >= len(current_playlist):
        raise HTTPException(status_code=404, detail="Song not found")

    current_song_index = index
    song = current_playlist[index]

    download_response = await download_mp3(url=song.videoUrl)
    if not download_response.data or not download_response.data.get("dl"):
        raise HTTPException(status_code=500, detail="Failed to get audio URL")

    download_url = download_response.data["dl"]
    add_to_recently_played(song)
    is_playing = True

    return JSONResponse(content={"status": True, "song": song.dict(), "download_url": download_url})

def add_to_recently_played(song: Song):
    global recently_played
    recently_played = [s for s in recently_played if s.id != song.id]
    recently_played.insert(0, song)
    if len(recently_played) > APP_DEFAULTS["MAX_RECENT_ITEMS"]:
        recently_played = recently_played[:APP_DEFAULTS["MAX_RECENT_ITEMS"]]

@app.get("/recently_played", tags=["Player"], description="Mendapatkan riwayat lagu yang diputar.")
async def get_recently_played():
    return JSONResponse(content={"recently_played": [song.dict() for song in recently_played]})

@app.get("/queue", tags=["Player"], description="Mendapatkan daftar antrean lagu.")
async def get_queue():
    queue = []
    for i in range(APP_DEFAULTS["MAX_QUEUE_ITEMS"]):
        next_index = (current_song_index + i + 1) % len(current_playlist)
        if next_index != current_song_index:
            queue.append(current_playlist[next_index].dict())
    return JSONResponse(content={"queue": queue})

@app.get("/next", tags=["Player"], description="Memutar lagu berikutnya dalam playlist.")
async def play_next():
    global current_song_index
    if is_shuffle:
        next_index = random.choice([i for i in range(len(current_playlist)) if i != current_song_index])
    else:
        next_index = (current_song_index + 1) % len(current_playlist)
    return await play_song(next_index)

@app.get("/previous", tags=["Player"], description="Memutar lagu sebelumnya dalam playlist.")
async def play_previous():
    global current_song_index
    previous_index = (current_song_index - 1 + len(current_playlist)) % len(current_playlist)
    return await play_song(previous_index)

@app.get("/toggle_shuffle", tags=["Player"], description="Mengaktifkan/menonaktifkan mode shuffle.")
async def toggle_shuffle():
    global is_shuffle
    is_shuffle = not is_shuffle
    return JSONResponse(content={"shuffle": is_shuffle})

@app.get("/toggle_repeat", tags=["Player"], description="Mengaktifkan/menonaktifkan mode repeat.")
async def toggle_repeat():
    global is_repeat
    is_repeat = not is_repeat
    return JSONResponse(content={"repeat": is_repeat})

@app.get("/download/{index}", tags=["Songs"], description="Mengunduh lagu berdasarkan indeks dalam playlist.")
async def download_current_song(index: int):
    if index < 0 or index >= len(current_playlist):
        raise HTTPException(status_code=404, detail="Song not found")

    song = current_playlist[index]
    download_response = await download_mp3(url=song.videoUrl)
    if not download_response.data or not download_response.data.get("dl"):
        raise HTTPException(status_code=500, detail="Failed to get download URL")

    return JSONResponse(content={"download_url": download_response.data["dl"]})
                                   
