2. Langkah Eksekusi (Praktik)
Buka terminal WSL kita, lalu jalankan simulasi ini secara berurutan sesuai panduan:

Ketik perintah ini: yes > /dev/null &

Penjelasan: Perintah yes itu fungsinya mencetak huruf "y" tanpa henti secepat mungkin (ini yang bikin CPU kerja keras). Tanda > /dev/null fungsinya membuang output-nya ke "tempat sampah" virtual biar terminal lu nggak penuh sama huruf "y". Tanda & di akhir memastikan proses ini berjalan secara background, jadi terminal kita masih bisa dipakai ngetik perintah lain.

Buka Monitor: Ketik htop

Penjelasan: Di sini kita bakal lihat grafik CPU lu (atau salah satu core-nya) langsung melonjak ke 100% dengan warna merah.

Hentikan Proses: Tekan q untuk keluar dari htop, lalu ketik killall yes

Penjelasan: Ini membuktikan kalau OS masih mendengarkan perintah kita untuk mematikan secara paksa proses yang bermasalah.

3. Jawaban Analitis 

Cara Identifikasi Proses: Saya mengidentifikasi proses tersebut menggunakan tools monitoring htop. Di sana terlihat jelas ada proses bernama yes yang menempati urutan teratas (Top) dan menghabiskan resource pada kolom %CPU hingga nyaris 100%.

Bagaimana OS Menanganinya: Meskipun proses yes memonopoli CPU secara intensif, sistem operasi tidak mengalami crash atau hang. Hal ini terjadi karena kernel Linux memiliki Process Scheduler yang melakukan context switching. OS tetap memberikan sedikit celah CPU agar perintah lain (seperti htop dan killall) tetap bisa dieksekusi.

Dampak Terhadap Sistem: Dampak langsungnya adalah peningkatan suhu prosesor (kipas laptop akan berputar kencang) dan keterlambatan respon (latency) jika kita mencoba menjalankan aplikasi lain secara bersamaan.
