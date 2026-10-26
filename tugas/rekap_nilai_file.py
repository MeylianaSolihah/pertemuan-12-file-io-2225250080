def baca_data(nama_file):
    data = []

    try:
        with open(nama_file, "r", encoding="utf-8-sig") as file:
            for baris in file:
                baris = baris.strip()

                if not baris:
                    continue

                try:
                    bagian = baris.split(",")

                    if len(bagian) != 2:
                        raise ValueError

                    nim = bagian[0].strip()
                    nilai = float(bagian[1].strip())

                    data.append((nim, nilai))

                except ValueError:
                    print(f"Data tidak valid, dilewati: {baris}")

    except FileNotFoundError:
        print(f"Error: File {nama_file} tidak ditemukan.")

    return data


def tulis_rekap(nama_file, data):
    with open(nama_file, "w", encoding="utf-8") as file:
        file.write("HASIL REKAP NILAI MAHASISWA\n")
        file.write("===========================\n")

        if not data:
            file.write("Tidak ada data nilai yang valid.\n")
            print("Tidak ada data valid untuk direkap.")
            return

        nilai_list = [nilai for nim, nilai in data]
        rata_rata = sum(nilai_list) / len(nilai_list)
        nilai_min = min(nilai_list)
        nilai_max = max(nilai_list)
        jumlah_lulus = sum(1 for nilai in nilai_list if nilai >= 60)

        file.write(f"Jumlah data valid: {len(data)}\n")
        file.write(f"Rata-rata nilai: {rata_rata:.2f}\n")
        file.write(f"Nilai minimum: {nilai_min:g}\n")
        file.write(f"Nilai maksimum: {nilai_max:g}\n")
        file.write(f"Jumlah lulus (nilai >= 60): {jumlah_lulus}\n")
        file.write("\nDAFTAR NILAI VALID\n")

        for nim, nilai in data:
            file.write(f"{nim}: {nilai:g}\n")

    print(f"Rekap berhasil disimpan ke {nama_file}")


if __name__ == "__main__":
    data = baca_data("data/nilai.txt")
    tulis_rekap("data/hasil_rekap.txt", data)
