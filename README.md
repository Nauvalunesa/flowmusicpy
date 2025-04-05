# Music Player Web Application
<p align="center">
  <img alt="screenshot" src="css/ss.jpg">
</p>

##  Overview

Music Player adalah aplikasi web yang memungkinkan pengguna mencari, memutar, dan mengunduh musik dari YouTube. Dirancang dengan fokus pada pengalaman pengguna yang baik, antarmuka yang responsif, dan fitur-fitur intuitif, Music Player menyediakan cara mudah untuk menikmati musik langsung di browser Anda.

## ✨ Features

-   **Pencarian Lagu** - Cari lagu, artis, atau album dari YouTube
-   **Pemutaran Langsung** - Putar musik langsung di browser tanpa perlu mengunduh terlebih dahulu
-   **Download MP3** - Unduh lagu yang sedang diputar dalam format MP3
-   **Riwayat Pemutaran** - Lihat dan akses kembali lagu-lagu yang baru saja diputar
-   **Antrian Lagu** - Lihat lagu berikutnya yang akan diputar dalam playlist
-   **Kontrol Pemutaran Lengkap**:
    -   Play/Pause
    -   Lompat ke lagu sebelumnya/berikutnya
    -   Mode shuffle untuk pemutaran acak
    -   Mode repeat untuk mengulang lagu saat ini
    -   Kontrol timeline (lompat ke bagian tertentu dari lagu)
-   **Responsive Design** - Tampilan yang optimal di desktop dan perangkat mobile
-   **Mini Player & Full Screen Mode** - Pilihan tampilan pemutaran yang fleksibel

##  Teknologi

Music Player dibangun dengan teknologi web dasar:

-   **HTML5** - Struktur dan markup
-   **CSS3** - Styling, animasi, dan responsivitas
-   **JavaScript** - Logika aplikasi dan interaksi pengguna
-   **Font Awesome** - Ikon-ikon UI
-   **FastAPI** - Backend API
-   **Siputz API** - API untuk pencarian YouTube dan konversi/download MP3

##  Struktur Project

Project menggunakan struktur modular dengan pemisahan frontend dan backend untuk memudahkan pengembangan dan pemeliharaan:


music-player/
├── backend/          # Direktori untuk kode backend (FastAPI)
│   ├── main.py       # File utama aplikasi FastAPI
│   └── config.py     # Konfigurasi backend
├── frontend/         # Direktori untuk kode frontend (HTML, CSS, JavaScript)
│   ├── index.html    # File HTML utama
│   ├── css/          # Direktori untuk stylesheet
│   │   └── style.css # Stylesheet utama
│   ├── js/           # Direktori untuk JavaScript
│   │   └── frontend.js # File JavaScript utama untuk frontend
│   └── assets/       # Direktori untuk aset (gambar, dll.)
│       └── ss.jpg     # Gambar preview (atau aset lainnya)
├── LICENSE           # Dokumen lisensi proyek
└── README.md          # Dokumen README proyek

## 🆕 Perubahan Terbaru

Beberapa perubahan terbaru pada aplikasi:

1.  **Pemisahan Backend dan Frontend** - Struktur proyek yang lebih terorganisir dengan pemisahan kode backend dan frontend.
2.  **API FastAPI** - Penggunaan FastAPI sebagai backend untuk pengelolaan API.
3.  **Konfigurasi API yang Disederhanakan** - Struktur konfigurasi API yang lebih sederhana dan direct.
4.  **Error Handling yang Lebih Robust** - Penanganan kesalahan yang lebih baik untuk stabilitas aplikasi.
5.  **Direct Data Access** - Pengambilan data yang lebih sederhana meningkatkan kinerja dan mengurangi error.
6.  **Animasi dan UI yang Ditingkatkan** - Pengalaman pengguna yang lebih mulus dengan animasi yang lebih baik.

##  Cara Penggunaan

## Instalasi dan Menjalankan Aplikasi dengan PM2

1.  **Clone repositori**
    ```bash
    git clone [https://github.com/Nauvalunesa/flowmusicpy.git](https://github.com/Nauvalunesa/flowmusicpy.git)
    ```
2.  **Buka folder proyek**
    ```bash
    cd flowmusicpy
    ```
3.  **Instalasi dependensi (Opsional tetapi disarankan)**
    * Jika proyek memiliki file `requirements.txt` di folder `backend`, instal dependensi Python:
        ```bash
        cd backend
        pip install -r requirements.txt
        cd ..
        ```
    * Jika menggunakan Node.js untuk frontend, instal dependensi Node.js di folder `frontend`
        ```bash
        cd frontend
        npm install
        cd ..
        ```
4.  **Menjalankan aplikasi dengan PM2**
    * Instal PM2 secara global (jika belum terinstal):
        ```bash
        npm install -g pm2
        ```
    * Jalankan backend FastAPI menggunakan PM2:
        ```bash
        cd backend
        pm2 start "python3 -m uvicorn main:app --host 0.0.0.0 --port 8000" --name fastapi
        cd ..
        ```
    * Buka file `frontend/index.html` di browser web favorit Anda, atau
    * Gunakan server lokal seperti Live Server extension di VSCode.
    * Jika menggunakan Node.js untuk frontend, anda bisa menjalankan server node.js dengan perintah `npm run dev` atau `npm run build` dan kemudian di serve menggunakan server statis. contoh:
        ```bash
        cd frontend
        npm run dev
        cd ..
        ```
        atau
        ```bash
        cd frontend
        npm run build
        npx serve dist
        cd ..
        ```
5.  **Pengelolaan PM2 (Opsional)**
    * Untuk melihat daftar proses PM2:
        ```bash
        pm2 list
        ```
    * Untuk melihat log aplikasi FastAPI:
        ```bash
        pm2 logs fastapi
        ```
    * Untuk menghentikan aplikasi FastAPI:
        ```bash
        pm2 stop fastapi
        ```
    * Untuk memulai ulang aplikasi FastAPI:
        ```bash
        pm2 restart fastapi
        ```
    * Untuk menghapus aplikasi FastAPI dari PM2:
        ```bash
        pm2 delete fastapi
        ```


### Penggunaan

1.  **Mencari Lagu**
    -   Masukkan judul lagu, nama artis, atau album di kotak pencarian
    -   Klik tombol "Cari" atau tekan Enter
2.  **Memutar Lagu**
    -   Klik pada hasil pencarian untuk memutar lagu
    -   Gunakan kontrol di mini player atau full player untuk mengontrol pemutaran
3.  **Mengunduh Lagu**
    -   Klik tombol "Download MP3" pada full player untuk mengunduh lagu yang sedang diputar
4.  **Melihat Riwayat Pemutaran**
    -   Riwayat pemutaran ditampilkan di halaman utama
    -   Klik pada lagu di riwayat untuk memutarnya kembali

##  Konfigurasi API

Aplikasi ini menggunakan konfigurasi API yang sederhana dan langsung:

```javascript
// API URLs - Basic configuration
const API_URL = {
    SEARCH: '[https://api.siputzx.my.id/api/s/youtube](https://api.siputzx.my.id/api/s/youtube)',
    DOWNLOAD_MP3: '[https://api.siputzx.my.id/api/d/ytmp3](https://api.siputzx.my.id/api/d/ytmp3)'
};

// App defaults
const APP_DEFAULTS = {
    DEFAULT_SEARCH: 'popular songs 2025',
    MAX_RECENT_ITEMS: 10,
    MAX_QUEUE_ITEMS: 5,
    STORAGE_KEY: 'recentlyPlayed'
};

Responsivitas
Music Player didesain untuk bekerja dengan baik di semua ukuran layar:
 * Desktop: Tampilan grid dan kontrol lengkap
 * Tablet: Tata letak yang dioptimalkan untuk layar menengah
 * Mobile: Antarmuka yang ramping dengan ukuran elemen yang disesuaikan
⚡ Tips Pengembangan
Jika Anda ingin mengembangkan aplikasi ini lebih lanjut:
 * Konfigurasi API:
   * File backend/config.py berisi semua pengaturan API dan nilai default
   * Ubah URL API dan pengaturan default sesuai kebutuhan
 * Styling:
   * Semua style ada di file /css/style.css
   * Styling terorganisasi berdasarkan komponen untuk kemudahan pengembangan
 * Logika Aplikasi:
   * Logika utama berada di /js/frontend.js
   * Fungsi-fungsi dikelompokkan berdasarkan fungsionalitas
 * Menambahkan Fitur Baru:
   * Tambahkan event listener baru di function setupEventListeners()
   * Tambahkan fungsi-fungsi baru yang terkait dengan fitur tersebut
Penanganan Error
Aplikasi ini menggunakan pendekatan robust untuk menangani error:
try {
    // Fetch data from the API
    const response = await fetch(`${API_URL.SEARCH}?query=${encodeURIComponent(query)}`);
    const data = await response.json();

    // Check if we have valid results
    if (!data.status || !data.data || data.data.length === 0) {
        noResultsElement.style.display = 'block';
        return;
    }

    // Proceed with valid data...
} catch (error) {
    console.error('Error fetching search results:', error);
    loadingElement.style.display = 'none';
    noResultsElement.style.display = 'block';
}

Kredit & Atribusi
 Siputz API - Untuk menyediakan API yang membuat music player ini mungkin
 YouTube - Sebagai sumber konten musik
 Font Awesome - Untuk ikon UI
 FastAPI - Untuk backend API
 FlowFalcon - Untuk pengembangan website Music Player
 Nauval - untuk ubah dari javascript ke python 
Kontak
Jika Anda memiliki pertanyaan, silakan hubungi:
 * Email: support@flowfalcon.xyz
 * GitHub: @FlowFalcon
 * WhatsApp: +62 851-2336-6391
Made with ❤️ by FlowFalcon

File `README.md` ini telah disesuaikan dengan struktur proyek yang baru, menggunakan FastAPI sebagai backend, dan perubahan-perubahan lainnya yang telah kita bahas.


