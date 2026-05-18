# NEMU IPB

NEMU IPB adalah platform digital terpusat untuk sistem pelaporan, pencarian, verifikasi, klaim, dan pengelolaan barang hilang dan ditemukan di lingkungan IPB University.

Sistem ini dikembangkan untuk menggantikan proses pelaporan barang hilang yang sebelumnya masih dilakukan secara informal menjadi sistem digital yang:
- terstruktur
- scalable
- mudah digunakan
- cepat diakses
- memiliki tracking status barang
- mendukung verifikasi admin
- mendukung proses klaim dan serah terima barang

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
