file1 = open("menu.txt","r")
file2 = open("Daftar Rumus.txt","a+")
x = []
teks = ["1. Lihat Rumus \n","2. Buat Rumus \n"]
print(file1.read())

perintah = input("Masukkan Perintah : ")
if perintah=="1":
    print(file2.read())
if perintah=="2":
    file2.write(input("Masukkan Judul : "))
    file2.writelines(x)
    print(file2.read())




