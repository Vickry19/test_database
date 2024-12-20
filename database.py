mahasiswa = [
    {"NIM": 123456, "Nama": "John", "Alamat": "Jl. Merdeka No. 1", "Jurusan": "Teknik Informatika", "Umur": 21},
    {"NIM": 234567, "Nama": "Alice", "Alamat": "Jl. Gatot Subroto", "Jurusan": "Sistem Informasi", "Umur": 23},
    {"NIM": 345678, "Nama": "Bob", "Alamat": "Jl. Sudirman No. 5", "Jurusan": "Teknik Informatika", "Umur": 20},
    {"NIM": 456789, "Nama": "Cindy", "Alamat": "Jl. Pahlawan No. 2", "Jurusan": "Manajemen", "Umur": 22},
    {"NIM": 567890, "Nama": "David", "Alamat": "Jl. Diponegoro No. 3", "Jurusan": "Teknik Elektro", "Umur": 25},
    {"NIM": 678901, "Nama": "Emily", "Alamat": "Jl. Cendrawasih No. 4", "Jurusan": "Manajemen", "Umur": 24},
    {"NIM": 789012, "Nama": "Frank", "Alamat": "Jl. Ahmad Yani No. 6", "Jurusan": "Teknik Informatika", "Umur": 19}
]

mata_kuliah = [
    {"ID": 1, "Mata_Kuliah": "Pemrograman Web", "NIM": 123456, "Nilai": 85, "Dosen_Pengajar": "Pak Budi"},
    {"ID": 2, "Mata_Kuliah": "Basis Data", "NIM": 234567, "Nilai": 70, "Dosen_Pengajar": "Ibu Ani"},
    {"ID": 3, "Mata_Kuliah": "Jaringan Komputer", "NIM": 345678, "Nilai": 75, "Dosen_Pengajar": "Pak Dodi"},
    {"ID": 4, "Mata_Kuliah": "Sistem Operasi", "NIM": 123456, "Nilai": 90, "Dosen_Pengajar": "Pak Budi"},
    {"ID": 5, "Mata_Kuliah": "Manajemen Proyek", "NIM": 456789, "Nilai": 80, "Dosen_Pengajar": "Ibu Desi"},
    {"ID": 6, "Mata_Kuliah": "Bahasa Inggris", "NIM": 567890, "Nilai": 85, "Dosen_Pengajar": "Ibu Eka"},
    {"ID": 7, "Mata_Kuliah": "Statistika", "NIM": 678901, "Nilai": 75, "Dosen_Pengajar": "Pak Farhan"},
    {"ID": 8, "Mata_Kuliah": "Algoritma", "NIM": 789012, "Nilai": 65, "Dosen_Pengajar": "Pak Galih"},
    {"ID": 9, "Mata_Kuliah": "Pemrograman Java", "NIM": 123456, "Nilai": 95, "Dosen_Pengajar": "Pak Budi"}
]

print("\n1. Mengubah alamat mahasiswa dengan NIM 123456")
print("Alamat sebelum diubah:")
for mhs in mahasiswa:
    if mhs["NIM"] == 123456:
        print(f"Nama: {mhs['Nama']}, Alamat: {mhs['Alamat']}")

        mhs["Alamat"] = "Jl. Raya No.5"
        print("Alamat setelah diubah:")
        print(f"Nama: {mhs['Nama']}, Alamat: {mhs['Alamat']}")

print("\n2. Daftar Mahasiswa Teknik Informatika dan Dosen Pembimbing:")
for mhs in mahasiswa:
    if mhs["Jurusan"] == "Teknik Informatika":
        print(f"\nData Mahasiswa:")
        print(f"NIM: {mhs['NIM']}")
        print(f"Nama: {mhs['Nama']}")
        print(f"Jurusan: {mhs['Jurusan']}")
        print("Dosen Pengajar:")

        for mk in mata_kuliah:
            if mk["NIM"] == mhs["NIM"]:
                print(f"- {mk['Dosen_Pengajar']} (Mata Kuliah: {mk['Mata_Kuliah']})")

print("\n3. Daftar 5 Mahasiswa Tertua:")

mahasiswa_urut = sorted(mahasiswa, key=lambda x: x["Umur"], reverse=True)

for i, mhs in enumerate(mahasiswa_urut[:5], 1):
    print(f"{i}. Nama: {mhs['Nama']}, Umur: {mhs['Umur']} tahun")

print("\n4. Daftar Nilai Mahasiswa (Nilai > 70):")
for mk in mata_kuliah:
    if mk["Nilai"] > 70:
        for mhs in mahasiswa:
            if mhs["NIM"] == mk["NIM"]:
                print(f"Nama: {mhs['Nama']}")
                print(f"Mata Kuliah: {mk['Mata_Kuliah']}")
                print(f"Nilai: {mk['Nilai']}")
                print("-" * 30)
