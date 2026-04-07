# 📘 Laporan Analisis Memory & Resource - Kelompok 1
**Analyst:** Desta Ardiansyah (Memory Analyst)
**Environment:** WSL 2 (Ubuntu 22.04)
**Objek Analisis:** Aplikasi Node.js & MySQL (Docker)

---

## I. Pendahuluan
Laporan ini bertujuan untuk mengamati bagaimana Sistem Operasi (melalui kernel Linux di WSL) mengalokasikan dan mengelola sumber daya memori (RAM) saat sebuah aplikasi berjalan.

## II. Langkah Kerja & Observasi
Langkah-langkah yang dilakukan untuk mengambil data:
1. Menjalankan perintah `free -m` di terminal WSL untuk melihat statistik penggunaan memori.
2. Mengamati penggunaan Swap memory untuk melihat apakah sistem melakukan paging ke disk.
3. Melakukan observasi melalui alat monitoring `htop` untuk identifikasi proses spesifik.

### A. Statistik Memori (Berdasarkan `free -m`)
Berdasarkan observasi langsung pada terminal, berikut adalah data penggunaan memori sistem:

| Kategori | Kapasitas (MB) |
| :--- | :--- |
| **Total Physical Memory (Mem)** | 7747 MB |
| **Used Memory** | 3878 MB |
| **Free Memory** | 3315 MB |
| **Shared Memory** | 29 MB |
| **Buff/Cache** | 773 MB |
| **Available Memory** | 3868 MB |
| **Swap Total** | 2048 MB |

---

## III. Analisis Sistem Operasi (Jawaban Pertanyaan)

### 1. Bagaimana OS mengalokasikan memori untuk proses?
Berdasarkan data di atas, OS mengalokasikan sekitar **3878 MB (Used)** untuk menjalankan berbagai proses, termasuk aplikasi Node.js dan MySQL. Sistem Operasi menggunakan teknik **Dynamic Memory Allocation**. Kernel Linux memberikan porsi memori dalam bentuk *Pages*. Jika aplikasi membutuhkan memori lebih dari yang tersedia secara fisik, OS akan menggunakan **Swap Memory** (terdeteksi digunakan sebesar 1 MB) sebagai area cadangan di disk.

### 2. Apa faktor yang mempengaruhi penggunaan memori tersebut?
Penggunaan memori sebesar **3878 MB** pada sistem ini dipengaruhi oleh beberapa faktor:
- **Runtime Environment:** Node.js memerlukan *Heap Memory* untuk engine V8 agar aplikasi biodata bisa berjalan.
- **Docker Containers:** Menjalankan MySQL dan phpMyAdmin di dalam container menambah beban memori karena setiap container memiliki isolasi resource-nya sendiri.
- **Buffer/Cache:** OS menyisihkan **773 MB** sebagai *cache* untuk mempercepat akses file (I/O), yang menunjukkan optimasi kernel Linux dalam manajemen file system.

## IV. Bukti Observasi
Berikut adalah tangkapan layar penggunaan memori saat sistem dalam kondisi operasional:

![Monitoring Memory via htop](ram_desta.png)

---
*Laporan ini disusun untuk memenuhi tugas besar Sistem Operasi berbasis WSL.*