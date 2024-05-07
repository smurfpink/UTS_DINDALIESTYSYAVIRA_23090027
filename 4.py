def kalkulator_bmi():
  berat = float(input('Masukkan berat badan Anda (kg): '))
  tinggi = float(input('Masukkan tinggi badan Anda (cm): '))

  tinggi /= 100

  bmi = berat / (tinggi ** 2)

  print(f'Indeks massa tubuh Anda adalah {bmi:.2f}')

  if bmi < 18.5:
    print('Kategori: Berat badan kurang')
  elif 18.5 <= bmi < 24.9:
    print('Kategori: Berat badan normal')
  elif 25 <= bmi < 29.9:
    print('Kategori: Kelebihan berat badan')
  else:
    print('Kategori: Obesitas')

kalkulator_bmi()