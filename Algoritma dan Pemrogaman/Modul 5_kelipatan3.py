print ("Angka genap dengan kecuali")
bil = 0
n = eval(input("Batas atas = "))
i = 2
x = eval(input("Pengecualian (dalam kelipatan) = "))
while i<=n:
    if not bil+i % x == 0:
        print("bilangan ",bil+i)
    i+=2
