bilangan = []
ganjil = []
genap = []
stop = False
x = 1
while not stop:
    bilangan_baru = input("Input Bilangan : ")
    bilangan.append(bilangan_baru)
    x+= 1
    lanjut = input("Tambah Bilangan (y/n) : ")
    if lanjut == "n":
        stop = True
    
for i in bilangan:
    if int(i)%2==0:
        genap.append(i)
for j in bilangan:
    if int(j)%2==1:
        ganjil.append(j)
print("-"*20)
print (bilangan)
("\n")
tampilkan = input("Tampilkan? (ganjil/genap) : ")
if tampilkan == "genap":
    print (genap)
    print ("Total Banyaknya Bilangan Genap adalah {}".format(len(genap)))
else:
    print (ganjil)
    print ("Total Banyaknya Bilangan Ganjil adalah {}".format(len(ganjil)))
