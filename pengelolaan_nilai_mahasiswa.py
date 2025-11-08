# ======================================================
# Program Pengelolaan Data Nilai Mahasiswa 
# ======================================================
# Fitur sesuai tugas praktikum:
# - List berisi data mahasiswa
# - Hitung nilai akhir & tentukan grade
# - Tampilkan tabel data 
# - Tambah data mahasiswa baru
# - Cari nilai tertinggi & terendah
# - Filter berdasarkan grade
# - Hitung rata-rata kelas
# ======================================================

mahasiswa = [
    {"nama": "Rifka", "nim": "123140024", "uts": 90, "uas": 90, "tugas": 95},
    {"nama": "Fajar", "nim": "123140025", "uts": 75, "uas": 70, "tugas": 80},
    {"nama": "Danju", "nim": "123140026", "uts": 60, "uas": 65, "tugas": 70},
    {"nama": "Martin", "nim": "123140027", "uts": 55, "uas": 50, "tugas": 60},
    {"nama": "Ken", "nim": "123140028", "uts": 90, "uas": 95, "tugas": 85},
]

# ------------------------------------------------------
# Fungsi Perhitungan & Penentuan Grade
# ------------------------------------------------------
def hitung_nilai_akhir(uts, uas, tugas):
    return (0.3 * uts) + (0.4 * uas) + (0.3 * tugas)

def tentukan_grade(nilai):
    if nilai >= 80:
        return "A"
    elif nilai >= 70:
        return "B"
    elif nilai >= 60:
        return "C"
    elif nilai >= 50:
        return "D"
    else:
        return "E"

# ------------------------------------------------------
# Fungsi Tampilan Tabel (Versi Rapi)
# ------------------------------------------------------
def tampilkan_data(data):
    print("="*79)
    print("| {:^3} | {:^10} | {:^20} | {:^7} | {:^7} | {:^7} | {:^6} |".format(
        "No", "NIM", "Nama", "UTS", "UAS", "Tugas", "Grade"))
    print("="*79)
    for i, m in enumerate(data, start=1):
        nilai_akhir = hitung_nilai_akhir(m["uts"], m["uas"], m["tugas"])
        grade = tentukan_grade(nilai_akhir)
        print("| {:>3} | {:<10} | {:<20} | {:>7.0f} | {:>7.0f} | {:>7.0f} | {:^6} |".format(
            i, m["nim"], m["nama"], m["uts"], m["uas"], m["tugas"], grade))
    print("="*79)

# ------------------------------------------------------
# Tambah Data Mahasiswa
# ------------------------------------------------------
def tambah_data():
    print("\n=== Tambah Data Mahasiswa Baru ===")
    nama = input("Masukkan Nama: ")
    nim = input("Masukkan NIM: ")
    uts = float(input("Masukkan Nilai UTS: "))
    uas = float(input("Masukkan Nilai UAS: "))
    tugas = float(input("Masukkan Nilai Tugas: "))
    mahasiswa.append({"nama": nama, "nim": nim, "uts": uts, "uas": uas, "tugas": tugas})
    print("Data berhasil ditambahkan!\n")

# ------------------------------------------------------
# Nilai Tertinggi & Terendah
# ------------------------------------------------------
def cari_nilai_tertinggi_terendah():
    nilai_akhir = [(m["nama"], hitung_nilai_akhir(m["uts"], m["uas"], m["tugas"])) for m in mahasiswa]
    tertinggi = max(nilai_akhir, key=lambda x: x[1])
    terendah = min(nilai_akhir, key=lambda x: x[1])
    print("\nMahasiswa Nilai Tertinggi : ", tertinggi[0], "-", tertinggi[1])
    print("Mahasiswa Nilai Terendah   : ", terendah[0], "-", terendah[1], "\n")

# ------------------------------------------------------
# Filter Berdasarkan Grade
# ------------------------------------------------------
def filter_berdasarkan_grade():
    g = input("Masukkan grade yang ingin difilter (A/B/C/D/E): ").upper()
    hasil = []
    for m in mahasiswa:
        nilai_akhir = hitung_nilai_akhir(m["uts"], m["uas"], m["tugas"])
        if tentukan_grade(nilai_akhir) == g:
            hasil.append(m)
    if hasil:
        tampilkan_data(hasil)
    else:
        print("Tidak ada mahasiswa dengan grade tersebut.\n")

# ------------------------------------------------------
# Rata-rata Nilai Kelas
# ------------------------------------------------------
def rata_rata_kelas():
    total = 0
    for m in mahasiswa:
        total += hitung_nilai_akhir(m["uts"], m["uas"], m["tugas"])
    rata = total / len(mahasiswa)
    print(f"\nRata-rata Nilai Akhir Kelas : {rata:.2f}")
    print(f"Grade Kelas : {tentukan_grade(rata)}\n")

# ------------------------------------------------------
# Menu Utama
# ------------------------------------------------------
def menu():
    while True:
        print("\n===== MENU PROGRAM NILAI MAHASISWA =====")
        print("1. Tampilkan Data Mahasiswa")
        print("2. Tambah Data Mahasiswa Baru")
        print("3. Cari Nilai Tertinggi & Terendah")
        print("4. Filter Berdasarkan Grade")
        print("5. Hitung Rata-rata Kelas")
        print("6. Keluar")
        pilihan = input("Pilih menu (1-6): ")

        if pilihan == "1":
            tampilkan_data(mahasiswa)
        elif pilihan == "2":
            tambah_data()
        elif pilihan == "3":
            cari_nilai_tertinggi_terendah()
        elif pilihan == "4":
            filter_berdasarkan_grade()
        elif pilihan == "5":
            rata_rata_kelas()
        elif pilihan == "6":
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.\n")

if __name__ == "__main__":
    menu()