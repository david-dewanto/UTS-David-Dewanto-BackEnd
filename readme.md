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

### Menjalankan Server Development
1. Jalankan server Django
   ```bash
   python manage.py runserver
   ```
2. Akses server di `http://localhost:8000`

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

## Kontribusi
Ini adalah proyek akademik dan tidak terbuka untuk kontribusi.

---

*Catatan: README ini merupakan bagian dari tugas mata kuliah PAWM II3140 dan mencakup informasi dasar tentang backend PCademy. Untuk informasi lebih detail, silakan merujuk ke dokumentasi lengkap di Edunex.*
