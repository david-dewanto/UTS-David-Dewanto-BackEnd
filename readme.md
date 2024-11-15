# PCademy Backend

## Proyek
Backend PCademy menggunakan Django framework untuk mendukung website pembelajaran interaktif pengenalan komputasi. Proyek ini dikembangkan sebagai bagian dari tugas mata kuliah PAWM II3140.

### Informasi Pengembang
- **Nama:** David Dewanto
- **NIM:** 18222027
- **Mata Kuliah:** PAWM II3140

## Struktur Proyek
```
UTS-David-Dewanto-BackEnd
├── Pipfile
├── Pipfile.lock
├── requirements.txt
├── manage.py
├── vercel.json
├── UTS/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── user/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── tests.py
    ├── urls.py
    ├── views.py
    └── migrations/
        └── __init__.py
```

## Teknologi yang Digunakan
- Python 3.12
- Django (Framework Web)
- Pipenv (Manajemen Dependensi)
- Vercel (Deployment)

## Fitur Backend
- Sistem autentikasi pengguna
- Manajemen data pengguna
- API endpoints untuk:
  - Pendaftaran pengguna
  - Login/logout
  - Manajemen sesi pembelajaran
  - Tracking progres pengguna

## Memulai Proyek

### Prasyarat
- Python 3.12 atau versi lebih baru
- pip (Python package manager)
- pipenv

### Instalasi
1. Clone repositori
   ```bash
   git clone [repository-url]
   ```

2. Masuk ke direktori proyek
   ```bash
   cd UTS-David-Dewanto-BackEnd
   ```

3. Instal dependensi menggunakan pipenv
   ```bash
   pipenv install
   ```
   
   Atau menggunakan pip
   ```bash
   pip install -r requirements.txt
   ```

4. Aktifkan virtual environment (jika menggunakan pipenv)
   ```bash
   pipenv shell
   ```

5. Jalankan migrasi database
   ```bash
   python manage.py migrate
   ```

### Menjalankan Server Development
1. Jalankan server Django
   ```bash
   python manage.py runserver
   ```
2. Akses server di `http://localhost:8000`

## Struktur Aplikasi

### Aplikasi User
- **models.py**: Mendefinisikan model data pengguna
- **views.py**: Logika untuk penanganan request
- **urls.py**: Konfigurasi routing
- **admin.py**: Konfigurasi admin panel

### Konfigurasi Utama (UTS/)
- **settings.py**: Pengaturan utama Django
- **urls.py**: URL routing utama
- **wsgi.py** & **asgi.py**: Konfigurasi server

## API Endpoints

### User Management
- `/api/user/register/`: Pendaftaran pengguna baru
- `/api/user/login/`: Login pengguna
- `/api/user/logout/`: Logout pengguna
- `/api/user/profile/`: Manajemen profil pengguna

## Deployment
Proyek dikonfigurasi untuk deployment di Vercel dengan file konfigurasi `vercel.json`.

### Langkah Deployment
1. Pastikan semua dependensi tercatat di `requirements.txt`
2. Konfigurasi environment variables di Vercel
3. Deploy menggunakan Vercel CLI atau GitHub integration

## Pengembangan

### Menambah Fitur Baru
1. Buat branch baru
2. Implementasi fitur
3. Jalankan tests
4. Buat migrasi jika diperlukan
   ```bash
   python manage.py makemigrations
   ```
5. Terapkan migrasi
   ```bash
   python manage.py migrate
   ```

### Testing
Jalankan tests dengan perintah:
```bash
python manage.py test
```

## Informasi Tambahan
Untuk dokumentasi lengkap dan detail proyek, silakan lihat laporan lengkap yang tersedia di Edunex.

## Kontribusi
Ini adalah proyek akademik dan tidak terbuka untuk kontribusi.

## Lisensi
Proyek ini dibuat untuk tujuan akademik. Hak cipta dilindungi.

---

*Catatan: README ini merupakan bagian dari tugas mata kuliah PAWM II3140 dan mencakup informasi dasar tentang backend PCademy. Untuk informasi lebih detail, silakan merujuk ke dokumentasi lengkap di Edunex.*
