file1 = open("Daftar Rumus.txt","r")
file2 = open("Daftar Rumus.txt","a+")
zzz=1
x = []
while zzz==1:
    print("-"*50)
    print ("1. Lihat Rumus \n2. Buat Rumus (Belum) \n3. Edit Rumus (Belum) \n4. Selesai")
    perintah = input("Masukkan Perintah : ")
    if perintah=="1":
        print(file1.read())
    elif perintah=="2":
        #file2.write(input("Masukkan Judul : "))
        #file2.writelines(x)
        #print(file2.read())
        #print()
        print("Input Error")
    elif perintah=="3":
        #print("pilih file yang akan di edit")
        #print(file3.read())
        #print()
        print("Input Error")
    elif perintah=="4":
        zzz=0




