bilangan = []
ganjil = []
genap = []
n=eval(input("Jumlah Bilangan yang akan dimasukkan : "))
i=1

while i<=n:
    bilangan.append(input("Masukkan Bilangan : "))
    i+=1
    
for x in bilangan:
    if int(x)%2==0:
        genap.append(x)
for y in bilangan:
    if int(y)%2==1:
        ganjil.append(y)
print("-"*50)
print (bilangan)
tampilkan = input("Tampilkan? (ganjil/genap) : ")
if tampilkan == "genap":
    print (genap)
    print ("Total Banyaknya Bilangan Genap adalah {}".format(len(genap)))
elif tampilkan == "ganjil":
    print (ganjil)
    print ("Total Banyaknya Bilangan Ganjil adalah {}".format(len(ganjil)))

