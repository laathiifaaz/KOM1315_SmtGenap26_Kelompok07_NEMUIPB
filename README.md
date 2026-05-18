# NEMU IPB

NEMU IPB adalah platform digital terpusat untuk sistem pelaporan, pencarian, verifikasi, klaim, dan pengelolaan barang hilang dan ditemukan di lingkungan IPB University.

---

# Tech Stack

## Frontend
- React JS
- Tailwind CSS
- React Router DOM
- React Class Component (OOP)

## Backend
- Python FastAPI

## Database
- PostgreSQL

## ORM
- SQLAlchemy

---

# Implementasi Keamanan Informasi

## Authentication
- JWT Authentication
- Login & Logout
- Token Validation

## Authorization
- Role-based Access Control
- Protected Route & Endpoint

## Accounting
- Activity Logging
- Tracking aktivitas admin dan user

## Data at Rest Encryption
- Password hashing menggunakan bcrypt
- Enkripsi data sensitif

## Digital Signature
- Digital signature dokumen serah terima
- Signature verification

## SHA256 Integrity
- Generate SHA256 hash dokumen
- Validasi integritas data

## Session Security
- Session validation
- Session expiration
- Secure token management

# Architecture

## Backend Architecture

```txt id="wxd5ku"
Controller/Route
    ↓
Service Layer
    ↓
Repository Layer
    ↓
ORM/Database
```

## Frontend Architecture

```txt id="ul1ndn"
Page/Class Component
    ↓
Service Layer
    ↓
ApiClient
    ↓
FastAPI Backend
```

---
