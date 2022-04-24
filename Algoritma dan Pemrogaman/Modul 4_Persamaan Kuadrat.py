import math
a = eval(input("Masukkan nilai a = "))
b = eval(input("Masukkan nilai b = "))
c = eval(input("Masukkan nilai c = "))
D = b**2 - 4*a*c

print("Persamaan Kuadrat = ", a,"x^2 + ", b,"x + ", c)

if D == 0 :
    x1 = x2 = -b/2*a
if D > 0 :
    x1 = (-b + math.sqrt(D))/2*a
    x2 = (-b - math.sqrt(D))/2*a

if D < 0 :
    x1 = -b / 2*a + (math.sqrt(-D)/2*a)
    x2 = -b / 2*a - (math.sqrt(-D)/2*a)

print ("x1 adalah = ", x1)
print ("x2 adalah = ", x2)

