panjang = int(input())
lebar = int(input())
luas = panjang * lebar
print(panjang * lebar)
if luas < 50:
    print("Kecil")
else:
    if luas >= 50 and luas < 100:
        print("Menengah")
    else:
        print("Besar")
