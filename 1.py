operasi = int(input('Pilih operasi 1(+),2(-),3(*),4(/): '))
bil1 = float(input('Masukkan bilangan pertama: '))
bil2 = float(input('Masukkan bilangan kedua: '))

if operasi == 1:
  print(bil1 + bil2)
elif operasi == 2:
  print(bil1 - bil2)
elif operasi == 3:
  print(bil1 * bil2)
elif operasi == 4:
  if bil2 != 0:
    print(bil1 / bil2)
  else:
    print('Error: Division by zero!')
else:
  print('Invalid choice')