# Модуль1
zahl=int(input('Введите меньшее число'))
zahl2=int(input('Введите большее число'))
b=0
for a in range (zahl,zahl2+1):
    b=str(a)
    print(b*a)
# Конец модуля 1
# Модуль 2
length=float(input('Введите длинну отрезка А'))
b=float(input('Введите длинну отрезка Б'))
while length>=b:
    length=length-b
print('Осталось незанятым: ',length)
# Конец модуля 2
# Модуль 3
N=int(input('Введите число эн'))
k=0
summ=0
while summ<N:
    k=k+1
    summ=summ+k
print(summ,'- это сумма чисел',k,'-а это получившееся число Ка')
# Конец модуля 3
# Модуль 4
P=float(input('Введите процентную ставку'))
summ=1000
monat=0
while summ<1100:
    monat=monat+1
    summ=summ+summ*P/100
print('Вложившись, Вы получите: ',summ,' За',monat,' месяцев')
# Конец модуля 4
# Модуль 5
zahl=int(input('Введите одно число: '))
zahl2=int(input('Введите другое число'))
while zahl!=0 and zahl2!=0:
    if zahl>zahl2:
        zahl=zahl%zahl2
    else:
        zahl2=zahl2%zahl
print('Без магии пива тут не получилось, но НОД= ',zahl+zahl2)
# Конец модуля 5
# Модуль 6
N=int(input('Введите чиселку Фибаначи: '))
z=1
a1=0
a2=1
while a2<N:
    z=z+1
    сумма=a1+a2
    a1=a2
    a2=сумма
print('Тут тоже без пива никуда... Вот номер числа Эн среди чисел Фибаначи: ',z)
