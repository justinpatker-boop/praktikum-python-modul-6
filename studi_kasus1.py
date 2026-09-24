mahasiswa = [
    ["Andi", "Informatika", 3.8],
    ["Budi", "PTIK", 3.6],
    ["Citra", "Informatika", 3.9]
]

prodi_ipk = {}
prodi_count = {}

for nama, prodi, ipk in mahasiswa:
    if prodi in prodi_ipk:
        prodi_ipk[prodi] += ipk
        prodi_count[prodi] += 1
    else:
        prodi_ipk[prodi] = ipk
        prodi_count[prodi] = 1

mhs_tertinggi = max(mahasiswa, key=lambda x: x[2])
mhs_terendah = min(mahasiswa, key=lambda x: x[2])

print("===== DATA MAHASISWA =====")
for i, (nama, prodi, ipk) in enumerate(mahasiswa, 1):
    print(f"{i}. {nama:<8} | {prodi:<11} | {ipk}")

print("\nRata-rata IPK per Prodi:")
for prodi in prodi_ipk:
    rata = prodi_ipk[prodi] / prodi_count[prodi]
    print(f"Rata-rata IPK {prodi}: {rata:.2f}")

print(f"\nIPK Tertinggi: {mhs_tertinggi[0]} ({mhs_tertinggi[2]})")
print(f"IPK Terendah : {mhs_terendah} ({mhs_terendah[2]})")
