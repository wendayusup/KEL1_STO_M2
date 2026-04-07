# Analisis Filesystem & Permission
Nama: Salwa
Tugas: Nomor 6

## 1. Lokasi Project (pwd)
Project ini dikerjakan di lingkungan WSL (Linux).
### 2. Detail Direktori (ls -l)
Berikut adalah daftar file dan izin akses (permissions) di dalam folder proyek:

total 20
-rw-r--r-- 1 salwatama salwatama  691 Apr  7 15:29 README.md
drwxr-xr-x 6 salwatama salwatama 4096 Apr  7 15:33 analysis
drwxr-xr-x 2 salwatama salwatama 4096 Apr  7 15:29 docs
drwxr-xr-x 2 salwatama salwatama 4096 Apr  7 15:29 laporan
drwxr-xr-x 2 salwatama salwatama 4096 Apr  7 15:29 src

### 3. Analisis Singkat
Berdasarkan hasil `ls -l`, file-file di folder ini rata-rata memiliki izin `rw-r--r--`. 
Artinya:
- **Owner (Salwa):** Bisa baca dan ubah file.
- **Group & Others:** Hanya bisa baca saja.