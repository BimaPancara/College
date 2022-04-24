#Seorang dosen Teknik Komputer telah memeriksa hasil ujian mahasiswa sekaligus menilainya. 
#Buatlah sebuah program menggunakan method yang dapat mengkonversi nilai 0-100 menjadi abjad.
#Jika nilai 0 - 20 akan muncul output ‘E’ dan ‘Mengulang’
#Jika nilai 21 - 40 akan muncul output ‘D’ dan “Mengulang’
#Jika nilai 41 - 60 akan muncul output ‘C’ dan ‘Mengulang’
#Jika nilai 61 - 80 akan muncul output ‘B’ dan ‘Lulus’
#Jika nilai 81 - 100 akan muncul output ‘A’ dan ‘Lulus’

nilai = eval(input("Masukkan Nilai : "))

if nilai<=20:
    print ("E dan Mengulang")
elif nilai>=21 and nilai<=40:
    print ("D dan Mengulang")
elif nilai>=41 and nilai<=60:
    print ("C dan Mengulang")
elif nilai>=61 and nilai<=80:
    print ("B dan Lulus")
elif nilai>=81 and nilai <=100:
    print ("A dan lulus")
