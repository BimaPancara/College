harga = eval(input("Total Harga Pembelian : "))
diskon = 0.1
dis = harga * diskon
bayar = harga - dis
if harga > 1500000:
    print ("Uang yang harus dibayarkan adalah Rp. {:0,.2f}".format(bayar))
else:
    print ("Uang yang harus dibayarkan adalah Rp. {:0,.2f}".format(harga))
