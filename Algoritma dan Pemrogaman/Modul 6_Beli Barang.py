n = eval(input("Total Barang Dibeli : "))
i=1
pembelian = []
while i<=n:
    harga_barang = eval(input("Harga Barang : "))
    jumlah_barang = eval(input("Jumlah Barang : "))
    total = harga_barang * jumlah_barang
    pembelian.append(total)
    i+=1

print ("Total Pembelian : Rp.{:0,.2f}".format(sum(pembelian)))

