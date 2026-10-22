import tkinter as tk
from tkinter import ttk

# Membuat jendela utama
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("450x600")
root.resizable(False, False)

# Judul aplikasi
judul = tk.Label(
    root,
    text="Aplikasi Prediksi Prodi Pilihan",
    font=("Arial", 16, "bold")
)
judul.pack(pady=20)

