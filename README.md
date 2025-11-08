# Program Pengelolaan Data Nilai Mahasiswa 

## Deskripsi
Program ini dibuat untuk memenuhi tugas praktikum **Program Pengelolaan Data Nilai Mahasiswa**, dengan tampilan tabel yang lebih rapi dan sejajar.

## Struktur Data
Data mahasiswa disimpan dalam bentuk **list of dictionary**, misalnya:
```python
mahasiswa = [
    {"nama": "Rifka", "nim": "123140024", "uts": 85, "uas": 90, "tugas": 80},
]
```

## Fitur Program
1. Menampilkan data mahasiswa dalam format tabel rapi
2. Menambah data mahasiswa baru
3. Mencari mahasiswa dengan nilai tertinggi & terendah
4. Filter berdasarkan grade (A–E)
5. Menghitung rata-rata nilai kelas
6. Keluar dari program

## Rumus
**Nilai Akhir = (0.3 × UTS) + (0.4 × UAS) + (0.3 × Tugas)**

**Grade:**
- A = ≥80
- B = ≥70
- C = ≥60
- D = ≥50
- E = <50

## Cara Menjalankan
1. Buka folder project di **VSCode**
2. Jalankan terminal
3. Ketik perintah:
   ```bash
   python pengelolaan_nilai_mahasiswa.py
   ```

## Contoh Hasil Tampilan
```
===============================================================================
| No  |    NIM     |        Nama         |   UTS   |   UAS   |  Tugas  | Grade |
===============================================================================
|   1 | 123140024  | Rifka               |      90 |      90 |      95 |  A    |
|   2 | 123140025  | Fajar               |      75 |      70 |      80 |  B    |
|   3 | 123140026  | Danju               |      60 |      65 |      70 |  C    |
|   4 | 123140027  | Martin              |      55 |      50 |      60 |  D    |
|   5 | 123140028  | Ken                 |      90 |      95 |      85 |  A    |
===============================================================================
```