Tahun = 0
while (Tahun < 1900 or Tahun > 2020):
    Tahun = eval(input("Masukkan Tahun: "))
if Tahun%4==0:
    print ("Tahun Kabisat")
else :
    print ("Bukan Tahun Kabisat")
