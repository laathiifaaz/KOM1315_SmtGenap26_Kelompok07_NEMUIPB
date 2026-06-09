# Informasi Source Code NEMU IPB

## Struktur Source Code

Repository ini terdiri dari dua bagian utama:

```text
backend/
frontend/
```

## Lokasi Service Backend

Beberapa service utama pada backend berada pada folder:

```text
backend/services/
```

Isi service backend meliputi:

```text
backend/services/
├── encryption/
├── EncryptionService.py
├── admin_activity_service.py
├── admin_analytics_service.py
├── auth_service.py
├── klaim_service.py
├── laporan_service.py
├── serah_terima_service.py
└── signature_service.py
```

## Informasi Fungsi Service

- `auth_service.py` digunakan untuk proses autentikasi pengguna, seperti login dan validasi user.
- `admin_activity_service.py` digunakan untuk mencatat aktivitas admin sebagai bagian dari audit log atau accounting.
- `admin_analytics_service.py` digunakan untuk kebutuhan analisis dan ringkasan data admin.
- `laporan_service.py` digunakan untuk pengelolaan laporan barang hilang dan barang ditemukan.
- `klaim_service.py` digunakan untuk proses klaim barang oleh pengguna.
- `serah_terima_service.py` digunakan untuk proses serah terima barang setelah klaim diverifikasi.
- `signature_service.py` digunakan untuk pembuatan dan verifikasi Digital Signature.
- `EncryptionService.py` dan folder `encryption/` digunakan untuk kebutuhan enkripsi data pada backend.

## Catatan Integrasi Digital Signature

Pada tahap pengembangan awal, implementasi Digital Signature dikembangkan sebagai komponen terpisah untuk kebutuhan implementasi dan pengujian keamanan informasi.

Pada versi pengumpulan ini, seluruh implementasi Digital Signature telah diintegrasikan ke dalam source code backend NEMU IPB sehingga tidak lagi menggunakan folder atau repository terpisah. Integrasi ini dilakukan agar seluruh mekanisme keamanan informasi berada dalam satu codebase yang terpusat, mudah diuji, dikelola, dan di-deploy.

Implementasi Digital Signature dapat ditemukan pada file:

```text
backend/services/signature_service.py
```

Sedangkan proses serah terima barang yang memanfaatkan mekanisme keamanan tersebut dapat ditemukan pada:

```text
backend/services/serah_terima_service.py
```

Digital Signature digunakan untuk menjamin keaslian dan integritas data pada proses serah terima barang. Mekanisme pembuatan dan verifikasi tanda tangan digital diimplementasikan pada `signature_service.py` dan digunakan oleh proses bisnis yang terdapat pada `serah_terima_service.py`.

## Fitur Keamanan yang Diimplementasikan

Seluruh fitur keamanan berikut telah terintegrasi dengan backend aplikasi NEMU IPB:

- Authentication menggunakan JWT
- Authorization berbasis Role-Based Access Control
- Accounting melalui Audit Log
- Data Integrity menggunakan SHA-256 Hashing
- Digital Signature
- Data Encryption
- Session Security

Dengan demikian, seluruh implementasi keamanan informasi pada NEMU IPB dapat ditemukan dan dijalankan langsung melalui source code yang terdapat pada folder `backend`.
