# Array berisi daftar nama mahasiswa
mahasiswa = ["Mute", "Jere", "Rahma", "Dina", "Aul"]

# Menampilkan semua nama
print("Daftar Mahasiswa:", mahasiswa)

# Mengakses elemen array
print("Mahasiswa pertama:", mahasiswa[0])

# Menambah data ke array
mahasiswa.append("Saleha")
print("Setelah ditambah:", mahasiswa)

# Menghapus elemen
mahasiswa.remove("Mute")
print("Setelah Mute dihapus:", mahasiswa)

# Dictionary 
mahasiswa = {
    "nama": "Muttia Zalzabila.S",
    "nim": "D0425502",
    "jurusan": "Teknik Sistem Informasi",
    "kelas": " A ",
    "angkatan": 2025,
    "alamat": "Polewali, Sulawesi Barat",

    "nilai": {
        "algoritma_pemrograman": 90,
        "struktur_data": 88,
        "basis_data": 93,
        "pemrograman_python": 95
    },

    "mata_kuliah_diambil": [
        "Algoritma Pemrograman",
        "Basis Data",
        "Pemrograman Python",
        "Kalkulus Informatika"
    ]
}

# Menampilkan seluruh data
print("\nData Mahasiswa:", mahasiswa)

# Mengakses data
print("Nama:", mahasiswa["nama"])
print("Kelas:", mahasiswa["kelas"])
print("Nilai Python:", mahasiswa["nilai"]["pemrograman_python"])

# Update nilai
mahasiswa["nilai"]["pemrograman_python"] = 98
print("Nilai Python Setelah Update:", mahasiswa["nilai"]["pemrograman_python"])
