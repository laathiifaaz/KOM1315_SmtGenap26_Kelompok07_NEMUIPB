# Informasi Source Code NEMU IPB

## Struktur Folder

```text
03_Source_Code/
├── backend/
├── frontend/
└── README.md
```

## Catatan Integrasi Digital Signature

Pada tahap pengembangan awal, modul Digital Signature dikembangkan sebagai komponen terpisah untuk kebutuhan implementasi dan pengujian fitur keamanan informasi.

Pada versi pengumpulan ini, seluruh source code Digital Signature telah diintegrasikan ke dalam folder **backend** sehingga tidak lagi memerlukan folder atau repository terpisah.

Seluruh implementasi keamanan sistem saat ini berada pada source code backend, meliputi:

- Authentication
- Authorization
- Accounting (Audit Log)
- Data Integrity (SHA-256)
- Digital Signature
- Session Security

Dengan demikian, untuk proses penilaian dan pengujian, seluruh kode terkait Digital Signature dapat ditemukan langsung pada folder:

```text
backend/
```

dan telah menjadi bagian dari aplikasi utama NEMU IPB.
