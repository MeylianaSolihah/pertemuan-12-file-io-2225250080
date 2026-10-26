with open("data/nilai.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()

        if not baris:
            continue

        try:
            nim, nilai = baris.split(",")
            nilai = float(nilai)
            print(f"NIM: {nim}, Nilai: {nilai}")
        except ValueError:
            print(f"Data tidak valid: {baris}")
