Jmlh_brg = int(input("Masukan jumlah barang: "))
total_Harga = 0

for i in range(Jmlh_brg):
    Harga = float(input(f"Masukan harga barang {i+1}: "))
    total_Harga += Harga

print(f"Total belanjaan: Rp{total_Harga:.2f}")