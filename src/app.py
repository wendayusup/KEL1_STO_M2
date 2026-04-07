import time
import os

print("========================================")
print("       Aplikasi Observasi OS Linux      ")
print("========================================")

# Mengambil Process ID (PID) secara otomatis untuk memudahkan Process Analyst
pid = os.getpid()
print(f"[INFO] PID Aplikasi ini: {pid}")

# Ini adalah alokasi memori dummy agar Memory Analyst bisa melihat
# ada pemakaian RAM saat script ini dicek di 'htop' atau 'free -m'
print("[INFO] Mengalokasikan dummy memory...")
dummy_memory = ['OS_ANALYSIS' * 1024 for _ in range(15000)] 

print("[INFO] Aplikasi berjalan stabil.")
print("[INFO] Biarkan terminal ini menyala dan buka terminal baru untuk htop.")
print("Tekan Ctrl+C untuk mematikan aplikasi.\n")

# Infinite loop supaya aplikasi gak langsung mati saat di-run
try:
    while True:
        time.sleep(2)
except KeyboardInterrupt:
    print("\n[INFO] Aplikasi dihentikan oleh user.")
