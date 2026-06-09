# Informasi Integrasi Keamanan Informasi NEMU IPB

## Catatan Integrasi Digital Signature

Pada pengembangan NEMU IPB, implementasi Digital Signature langsung diintegrasikan ke dalam backend utama agar seluruh mekanisme keamanan informasi berada dalam satu codebase yang terpusat, lebih mudah dikelola, diuji, dan di-deploy.

Dengan demikian, tidak terdapat folder Digital Signature terpisah pada repository ini karena seluruh implementasinya telah menjadi bagian dari backend aplikasi.

Implementasi utama Digital Signature dapat ditemukan pada:

```text
backend/services/signature_service.py
```

Digital Signature tersebut digunakan pada proses serah terima barang yang terdapat pada:

```text
backend/services/serah_terima_service.py
```

Mekanisme ini digunakan untuk menjamin keaslian (authenticity) dan integritas (integrity) data selama proses serah terima barang.

---

## File Keamanan Informasi yang Terintegrasi di Backend

Seluruh implementasi keamanan informasi berada pada folder:

```text
backend/services/
```

File yang terkait langsung dengan keamanan informasi meliputi:

### Authentication

```text
auth_service.py
```

Digunakan untuk proses autentikasi pengguna menggunakan JWT, login, validasi identitas pengguna, dan pengelolaan sesi.

### Accounting (Audit Log)

```text
admin_activity_service.py
```

Digunakan untuk mencatat aktivitas penting yang dilakukan admin sebagai bentuk audit trail dan akuntabilitas sistem.

### Digital Signature

```text
signature_service.py
```

Digunakan untuk pembuatan dan verifikasi tanda tangan digital guna menjamin keaslian dan integritas data.

### Implementasi Proses Serah Terima

```text
serah_terima_service.py
```

Mengimplementasikan proses bisnis serah terima barang yang memanfaatkan Digital Signature.

### Data Encryption

```text
EncryptionService.py
encryption/
```

Digunakan untuk proses enkripsi dan dekripsi data yang memerlukan perlindungan tambahan saat penyimpanan maupun pemrosesan.

---

## Implementasi Keamanan Informasi

Berdasarkan source code yang terdapat pada backend, NEMU IPB mengimplementasikan:

- Authentication
- Authorization (Role-Based Access Control)
- Accounting (Audit Log)
- Data Encryption
- Data Integrity
- Digital Signature
- Session Security

Seluruh implementasi tersebut telah terintegrasi ke dalam backend utama aplikasi NEMU IPB dan tidak dipisahkan ke repository maupun folder tersendiri.
