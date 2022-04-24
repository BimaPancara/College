print('Tebak Bilangan Acak')
from random import randint
bayam=randint(1,10)
kangkung=eval(input('Enter your guess: '))
if kangkung==bayam:
    print('You got it')
else:
    print('Sorry, the number is ', bayam)

print('')

print('Pemasukan Nilai Sederhana')
brokoli=eval(input('Enter grade: '))
if brokoli>=80 and brokoli<90:
    print('Your grade is a B')

print('')

print('Time dan score dengan if, dan if not')
sawi=eval(input('Masukkan Score: '))
cabai=eval(input('Masukkan Time: '))
if (sawi>1000 or cabai>20):
    print('Game over')
if not(sawi>1000 or cabai>20):
    print('Game continues.')

print('')

print('Giliran tersisa')
score=eval(input('Masukkan score: '))
time=eval(input('Masukkan time: '))
if score<1000 or time>20 and turns_remaining==0:
    print('Game Over')

print('')

print('Menentukan nilai menggunakan if and')
buncis = eval(input('Enter your score: '))
if buncis>=90:
    print('A')
if buncis>=80 and buncis<90:
    print('B')
if buncis>=70 and buncis<80:
    print('C')
if buncis>=60 and buncis<70:
    print('D')
if buncis<60:
    print('F')

print('')

print('Menentukan nilai menggunakan if , elif, dan else')
grade = eval(input('Enter your score: '))
if grade>=90:
    print('A')
elif grade>=80:
    print('B')
elif grade>=70:
    print('C')
elif grade>=60:
    print('D')
else:
    print('F')
