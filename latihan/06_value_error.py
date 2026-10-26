try:
    angka = float(input("Masukkan sebuah angka: "))
    print(f"Angka yang dimasukkan: {angka}")

except ValueError:
    print("Error: Input harus berupa angka.")
