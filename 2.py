Tahun = int(input("Masukan Tahun: "))

if (Tahun % 400 == 0) or ((Tahun % 4 == 0) and (Tahun % 100 != 0)):
    print("Tahun {0} merupakan Tahun Kabisat".format(Tahun))
else:
    print("Tahun {0} bukan merupakan Tahun Kabisat".format(Tahun))