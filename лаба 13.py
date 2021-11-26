# Модуль 1
a=float(input('Введите стоимость конфет за кило: '))
b=float(input('Введите количество граммов конфет, нужных для подсчёта: '))
print((a*b)/1000,' - Стоимость ', b, 'граммов конфет, при цене ', a, 'денег за кило' )
# Конец модуля 1
# Модуль 2
l=int(input())
Shritt=1
zahl=1
while Shritt<l+0.1:
    zahl=zahl*Shritt
    Shritt=Shritt+0.1
print(zahl)  
#Конец модуля 2
# Модуль3
v=int(input(''))
g=0
for r in range (1,2*v,2):
    g=g+r
    print(g)
#Конец модуля 3
# Модуль 4
number=float(input('Введите вещественное число А: '))
number2=int(input('Введите, в какую степень нужно возвести число: '))
number3=1
for i in range(1,number2+1):
    number3=number3+number**i
print(number3)
#Конец модуля 4
# Модуль 5
nummer=float(input('Введите число: '))
nummer2=int(input('Введите степень числа: '))
nummer3=1
nummer=abs(nummer)
nummer=nummer*(-1)
for v in range(1,nummer2+1):
    nummer3=nummer3+nummer**v
print(nummer3)
    
