# backend/config.py

# API URLs - Basic configuration
API_URL = {
    'SEARCH': 'https://api.siputzx.my.id/api/s/youtube',
    'DOWNLOAD_MP3': 'https://api.siputzx.my.id/api/d/ytmp3'
}

# App defaults
APP_DEFAULTS = {
    'DEFAULT_SEARCH': 'popular songs 2025',
    'MAX_RECENT_ITEMS': 10,
    'MAX_QUEUE_ITEMS': 5,
    'STORAGE_KEY': 'recentlyPlayed'
}

# Utility functions
def format_time(seconds: float) -> str:
    minutes = int(seconds / 60)
    secs = int(seconds % 60)
    return f"{minutes}:{secs:02}"

def needs_scrolling(text: str, max_length: int = 20) -> bool:
    return len(text) > max_length

def format_song(item: dict) -> dict:
    return {
        'id': item.get('videoId', ''),
        'title': item.get('title', 'Unknown Title'),
        'artist': item.get('author', {}).get('name', 'Unknown Artist'),
        'thumbnail': item.get('thumbnail', item.get('image', '/api/placeholder/300/300')),
        'duration': item.get('seconds', item.get('duration', {}).get('seconds', 0)),
        'timestamp': item.get('timestamp', item.get('duration', {}).get('timestamp', '0:00')),
        'videoUrl': item.get('url', '')
    }

def format_search_results(items: list) -> list:
    if not isinstance(items, list):
        return []
    return [format_song(item) for item in items]

def get_download_url(data: dict) -> Optional[str]:
    return data.get('dl') if data and data.get('dl') else None
  
