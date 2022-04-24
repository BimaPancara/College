#Modul 2
temp = eval(input('Masukkan suhu dalam Celsius: '))
f_temp = 9/5*temp+32
print('Pada Fahrenheit, suhu tersebut adalah', f_temp)
if f_temp > 212:
    print('Suhu tersebut diatas titik didih air.')
if f_temp < 32:
    print('Suhu tersebut dibawah titik beku air')
