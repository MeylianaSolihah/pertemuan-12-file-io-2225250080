# Pertemuan 12 - File Input-Output dan Penanganan Error Dasar

**Nama:** Meyliana Solihah  
**NIM:** 2225250080  
**Kelas:** 3B  
**Program Studi:** S1 Pendidikan Matematika

## Deskripsi
Proyek ini mempelajari cara menulis, membaca, dan menambahkan isi file menggunakan Python, serta menangani error dasar.

## Struktur Folder
- `data/`: menyimpan file catatan, nilai, dan hasil rekap.
- `latihan/`: berisi enam latihan file input-output dan penanganan error.
- `tugas/`: berisi program rekap nilai mahasiswa.

## Cara Menjalankan
Jalankan perintah berikut melalui terminal:

1. `python latihan/01_tulis_file.py`
2. `python latihan/02_baca_file.py`
3. `python latihan/03_append_file.py`
4. `python latihan/04_proses_baris.py`
5. `python latihan/05_file_not_found.py`
6. `python latihan/06_value_error.py`
7. `python tugas/rekap_nilai_file.py`

Sesuaikan perintah dengan lokasi folder proyek jika diperlukan.

## Format Data
File `data/nilai.txt` menggunakan format NIM,nilai. Contoh:

- `A001,85`
- `A002,78`
- `A003,92`
- `A004,abc`

Data dengan nilai yang tidak valid akan dilewati.

## Hasil Pengujian
Berdasarkan data contoh, program menghasilkan:
- Jumlah data valid: 5
- Rata-rata nilai: 83.40
- Nilai minimum: 74
- Nilai maksimum: 92
- Jumlah lulus (nilai >= 60): 5

## Refleksi
Melalui latihan ini, saya mempelajari cara mengelola file menggunakan Python, memproses data per baris, dan menangani kesalahan menggunakan `try-except`. Program rekap juga membantu memahami penggunaan fungsi untuk mengolah data dan menyimpan hasilnya ke file.

## Catatan Pengembangan
Proyek ini terdiri dari enam latihan dan satu tugas utama rekap nilai mahasiswa.

## Evaluasi Pembelajaran
Program telah diuji untuk membaca file, memproses data valid, melewati data tidak valid, dan menyimpan hasil rekap.
