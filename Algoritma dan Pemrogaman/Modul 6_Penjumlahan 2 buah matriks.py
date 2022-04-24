print ("[",end=" ")
for A in range (1,4):
    print (A, end=" ")
print ("]")

print ("[",end=" ")
for B in range (2,5):
    print (B, end=" ")
print ("]")

awal = 2
print ("[",end=" ")
for A in range (1,4):
    for B in range (awal,5,5):
        print (A+B, end=" ")
print ("]")
