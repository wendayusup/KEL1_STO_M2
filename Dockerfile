# Gunakan base image Python yang ringan
FROM python:3.11-slim

# Set folder kerja di dalam kontainer
WORKDIR /app

# Salin semua isi folder src dari laptop ke folder /app di kontainer
COPY src/ .

# Perintah untuk menjalankan aplikasi Rifki
# (Pastikan Rifki menamai filenya app.py)
CMD ["python", "app.py"]
