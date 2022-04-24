string = "1."

x = 7
bar = x
#baris
while bar >= 0:
        #kolom kosong
        kol = bar
        while kol > 0:
            string = string + " "
            kol = kol - 1
        #kolom pagar
        kanan = 1
        while kanan < (x - (bar-1)):
            string = string + "#"
            kanan = kanan + 1

        string = string + "\n"
        bar = bar - 1
        
print (string)
