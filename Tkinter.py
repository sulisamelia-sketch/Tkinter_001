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

# Frame untuk input nilai
frame_input = tk.Frame(root)
frame_input.pack(pady=5)

# Daftar mata pelajaran
mata_pelajaran = [
    "Nilai Mata Pelajaran 1",
    "Nilai Mata Pelajaran 2",
    "Nilai Mata Pelajaran 3",
    "Nilai Mata Pelajaran 4",
    "Nilai Mata Pelajaran 5",
    "Nilai Mata Pelajaran 6",
    "Nilai Mata Pelajaran 7",
    "Nilai Mata Pelajaran 8",
    "Nilai Mata Pelajaran 9",
    "Nilai Mata Pelajaran 10"
]

# Menyimpan input nilai
input_nilai = []

# Membuat 10 label dan input nilai
for i, mapel in enumerate(mata_pelajaran):
    label = tk.Label(
        frame_input,
        text=f"{mapel}:",
        width=20,
        anchor="w"
    )
    label.grid(row=i, column=0, padx=10, pady=5)
   
    entry = ttk.Entry(frame_input, width=15)
    entry.grid(row=i, column=1, padx=10, pady=5)
   
    input_nilai.append(entry)
   
   # Fungsi hasil prediksi
    def hasil_prediksi():
          hasil.config(
              text="Hasil Prediksi: Teknologi Informasi"
          )
     # Tombol prediksi
    tombol = tk.Button(
              root,
              text="Hasil Prediksi",
              command=hasil_prediksi,
              font=("Arial", 11, "bold"),
              bg="lightblue",
              width=20
          )
    tombol.pack(pady=20)
          
    # Label hasil prediksi
    hasil = tk.Label(
                  root,
                  text="Hasil Prediksi: Belum tersedia",
                  font=("Arial", 12, "bold"),
                  fg="blue"
              )
    hasil.pack(pady=10)
              
    # Menjalankan aplikasi
    root.mainloop()
                  
    