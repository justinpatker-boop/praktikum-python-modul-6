daftar_barang = []
total_harga = 0

while True:
    nama_barang = input("Masukkan nama barang: ")
    if nama_barang.lower() == "selesai":
        break
    harga = int(input("Masukkan harga: "))
    daftar_barang.append((nama_barang, harga))
    total_harga += harga

diskon = 0
if total_harga > 500000:
    diskon = 10

potongan = total_harga * diskon / 100
total_bayar = total_harga - potongan

print(f"\nTotal: {total_harga}")
print(f"Diskon: {diskon}%")
print(f"Total Bayar: {int(total_bayar)}")