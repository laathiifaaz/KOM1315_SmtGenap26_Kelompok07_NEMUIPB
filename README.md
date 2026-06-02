# NEMU IPB - Keamanan Informasi

## 1. Deskripsi Proyek

NEMU IPB adalah aplikasi web lost and found untuk civitas akademika IPB. Sistem ini membantu pengguna melaporkan barang hilang, melaporkan barang temuan, mengajukan klaim barang, melakukan dropoff barang temuan, serta membantu admin melakukan verifikasi laporan, klaim, dropoff, monitoring status, notifikasi, activity log, dashboard/analisis, dan serah terima barang.

Dokumen ini berfokus pada aspek Keamanan Informasi dalam sistem NEMU IPB. Sistem dirancang dengan pemisahan frontend, backend, dan database:

- Frontend: React
- Backend: FastAPI
- Database: PostgreSQL
- ORM: SQLAlchemy
- Migration: Alembic

Aspek keamanan informasi yang menjadi perhatian utama:

- Autentikasi pengguna melalui login.
- Otorisasi berdasarkan role `civitas` dan `admin`.
- Password hashing agar password tidak disimpan dalam bentuk plaintext.
- Token/session validation pada endpoint protected.
- HTTPS untuk komunikasi aman pada environment production.
- CORS untuk membatasi origin frontend yang boleh mengakses API.
- Activity log sebagai audit trail aktivitas penting admin.
- Digital signature dan document hashing untuk menjaga integritas dokumen serah terima.
- Secret management melalui environment variable.

Catatan: README ini hanya menjelaskan deskripsi proyek dan panduan instalasi. Tidak ada perubahan kode aplikasi yang dilakukan.

## Struktur Repository

```text
KOM1315_SmtGenap26_Kelompok07_NEMUIPB/
│
├── 01_Proposal_&_Analisis/
├── 02_Design_Documents/
├── 03_Source_Code/
│   ├── frontend/
│   ├── backend/
│   └── digital_signature/
├── 04_Reports_&_Paper/
│   ├── Monitoring_P7/
│   ├── Final_Technical_Report/
│   └── Scientific_Paper/
└── README.md
```

## 2. Panduan Instalasi

### 2.1 Prasyarat

Pastikan perangkat sudah memiliki:

- Python 3.10 atau versi yang kompatibel
- Node.js dan npm atau yarn
- PostgreSQL
- Git

### 2.2 Instalasi Backend FastAPI

Masuk ke folder backend:

```bash
cd backend
```

Buat dan aktifkan virtual environment:

```bash
python -m venv .venv
```

Windows:

```powershell
.\.venv\Scripts\activate
```

Mac/Linux:

```bash
source .venv/bin/activate
```

Install dependensi backend:

```bash
pip install -r requirements.txt
```

### 2.3 Konfigurasi Environment Backend

Buat file `.env` pada backend atau root project sesuai konfigurasi aplikasi. Contoh environment variable:

```env
DATABASE_URL=postgresql+psycopg2://username:password@localhost:5432/nemuipb
SECRET_KEY=isi_secret_key_yang_panjang_dan_acak
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
FERNET_KEY=isi_fernet_key_valid
```

Keterangan:

- `DATABASE_URL` digunakan untuk koneksi PostgreSQL.
- `SECRET_KEY` digunakan untuk JWT/token.
- `ALGORITHM` digunakan untuk algoritma token.
- `ACCESS_TOKEN_EXPIRE_MINUTES` digunakan untuk masa berlaku token.
- `FERNET_KEY` digunakan oleh encryption service.

Tips keamanan:

- Jangan commit file `.env` ke repository.
- Gunakan secret yang panjang, acak, dan berbeda untuk setiap environment.
- Simpan secret production di environment variable hosting atau secret manager.

### 2.4 Menjalankan PostgreSQL dan Alembic Migration

Pastikan service PostgreSQL berjalan, lalu buat database untuk NEMU IPB.

Contoh pembuatan database melalui PostgreSQL:

```sql
CREATE DATABASE nemuipb;
```

Pastikan `DATABASE_URL` sudah mengarah ke database tersebut.

Jalankan migration dari folder backend:

```bash
alembic upgrade head
```

Alembic digunakan untuk menjaga konsistensi struktur database, termasuk tabel penting seperti `users`, `sessions`, `barang`, `laporan`, `klaim_barang`, `notifikasi`, `serah_terima`, `activity_logs`, dan `alembic_version`.

### 2.5 Menjalankan Backend

Dari folder backend:

```bash
uvicorn app.main:app --reload
```

Backend lokal umumnya berjalan di:

```text
http://127.0.0.1:8000
```

Swagger API dapat diakses di:

```text
http://127.0.0.1:8000/docs
```

### 2.6 Instalasi Frontend React

Masuk ke folder frontend:

```bash
cd frontend
```

Install dependensi dengan npm:

```bash
npm install
```

Atau jika menggunakan yarn:

```bash
yarn install
```

### 2.7 Konfigurasi Environment Frontend

Buat file `.env` pada folder frontend dan isi base URL API:

```env
REACT_APP_API_BASE_URL=http://127.0.0.1:8000
```

Untuk production, gunakan URL backend HTTPS:

```env
REACT_APP_API_BASE_URL=https://domain-backend-production
```

Tips keamanan:

- Pada production, frontend HTTPS harus memanggil backend HTTPS.
- Hindari mixed content, yaitu frontend HTTPS memanggil backend HTTP.
- Pastikan backend mengizinkan origin frontend yang valid melalui CORS.

### 2.8 Menjalankan Frontend

Dari folder frontend:

```bash
npm start
```

Atau dengan yarn:

```bash
yarn start
```

Frontend lokal umumnya berjalan di:

```text
http://localhost:3000
```

## 3. Catatan Keamanan Informasi

- Gunakan HTTPS untuk backend dan frontend pada environment production.
- Jangan commit `SECRET_KEY`, `FERNET_KEY`, `DATABASE_URL`, atau file `.env`.
- Gunakan token/session validation untuk semua endpoint protected.
- Pastikan endpoint admin hanya dapat diakses oleh role `admin`.
- Batasi CORS hanya ke origin frontend yang resmi.
- Gunakan password hashing, bukan penyimpanan password plaintext.
- Pastikan activity log mencatat aktivitas penting seperti verifikasi laporan, klaim, dropoff, dan perubahan status.
- Jalankan Alembic migration secara konsisten agar schema database sesuai dengan kode.
- Lakukan backup database secara berkala.
- Pertimbangkan rate limiting pada endpoint login untuk mengurangi risiko brute force.
