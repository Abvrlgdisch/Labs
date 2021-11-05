# Модуль 1
a=int(input('Введите число: '))
b=int(input('Введите месяц: '))
if a==1:
    a=('Первое')
elif a==2:
    a=('Второе')  
elif a==3:
    a=('Третье')
elif a==4:
    a=('Четвёртое')
elif a==5:
    a=('Пятое')
elif a==6:
    a=('Шестое')
elif a==7:
    a=('Седьмое')
elif a==8:
    a=('Восьмое')
elif a==9:
    a=('Девятое')
elif a==10:
    a=('Десятое')
elif a==11:
    a=('Одиннадцатое')
elif a==12:
    a=('Двенадцатое')
elif a==13:
    a=('Тринадцатое')
elif a==14:
    a=('Четырнадцатое')
elif a==15:
    a=('Пятнадцатое')
elif a==16:
    a=('Шестнадцатое')
elif a==17:
    a=('Семнадцатое')
elif a==18:
    a=('Восемнадцатое')
elif a==19:
    a=('Девятнадцатое')
elif a==20:
    a=('Двадцатое')
elif a==21:
    a=('Двадцать первое')
elif a==22:
    a=('Двадцать второе')
elif a==23:
    a=('Двадцать третье')
elif a==24:
    a=('Двадцать четвёртое')
elif a==25:
    a=('Двадцать пятое')
elif a==26:
    a=('Двадцать шестое')
elif a==27:
    a=('Двадцать седьмое')
elif a==28:
    a=('Двадцать восьмое')
elif a==29:
    a=('Двадцать девятое')
elif a==30:
    a=('Тридцатое')
else:
    a=('Тридцать первое')
if b==1:
    b=('Января')
elif b==2:
    b=('Февраля')
elif b==3:
    b=('Марта')
elif b==4:
    b=('Апреля')
elif b==5:
    b=('Мая')
elif b==6:
    b=('Июня')
elif b==7:
    b=('Июля')
elif b==8:
    b=('Августа')
elif b==9:
    b=('Сентября')
elif b==10:
    b=('Октября')
elif b==11:
    b=('Ноября')
else:
    b=('Декабря')
print(a,b)
# Конец модуля 1
#Модуль 2
c=input('Введите направление: ')
n=int(input('Введите команду в соответствии с кодировкой: '))
if c=='Север':
    a=0
if c=='Запад':
    a=1
if c==('Юг'):
    a=2
if c=='Восток':
    a=3
Richtung=a-n
if Richtung>3:
    Richtung=Richtung-4
if Richtung<0:
    Richtung=Richtung+4
if Richtung==0:
    print('Север')
elif Richtung==1:
    print('Запад')
elif Richtung==2:
    print('Юг')
elif Richtung==3:
    print('Восток')
# Конец модуля 2
# Модуль 3
text='учебное задание'
text2='учебных заданий'
text3='учебных задания'
a=int(input('Введите количество учебных заданий: '))
if 30>a>20:
    print('двадцать ', end='')
    a=a-20
elif 40>a>30:
    print('тридцать ', end='')
    a=a-30
elif a==40:
    print('Сорок', text2)
elif a==30:
    print('Тридцать',text2)
if a==1:
    print('одно', text)
elif a==2:
    print('два', text2)
elif a==3:
    print('три',text3 )
elif a==4:
    print('Четыре', text3)
elif a==5:
    print('Пять',text2 )
elif a==6:
    print('шесть')
elif a==7:
    print('семь', text2)
elif a==8:
    print('восемь', text2)
elif a==9:
    print('девять', text2)
elif a==10:
    print('десять', text2)
elif a==11:
    print('одиннадцать', text2)
elif a==12:
    print('двенадцать', text2)
elif a==13:
    print('тринадцать', text2)
elif a==14:
    print('четырнадцать',text2)
elif a==15:
    print('пятнадцать',text2)
elif a==16:
    print('шестнадцать',text2)
elif a==17:
    print('семнадцать', text2)
elif a==18:
    print('восемнадцать', text2)
elif a==19:
    print('девятнадцать', text2)
elif a==20:
    print('двадцать', text2)
# Конец модуля 3
# Модуль 4
b=int(input('Введите чиселку: '))
if 1000>b>899:
    b=b-900
    print('Девятьсот ', end='')
elif 900>b>799:
    b=b-800
    print('Восемсот ', end='')
elif 800>b>699:
    b=b-700
    print('Семьсот ', end='')
elif 700>b>599:
    b=b-600
    print('Шестьсот ', end='')
elif 600>b>499:
    b=b-500
    print('Пятьсот ',end='')
elif 500>b>399:
    b=b-400
    print('Четыреста ', end='')
elif 400>b>299:
    b=b-300
    print('триста ', end='')
elif 300>b>199:
    b=b-200
    print('Двести ', end='')
elif 200>b>99:
    b=b-100
    print('Сто ', end='')
v=b
if 100>v>89:
    v=v-90
    print('Девяносто ', end='')
elif 90>v>79:
    v=v-80
    print('Восемьдесят ', end='')
elif 80>v>69:
    v=v-70
    print('Семьдясят', end='')
elif 70>v>59:
    v=v-60
    print('шестьдясят ',end='')
elif 60>v>49:
    v=v-50
    print('Пятьдесят ', end='')
elif 50>v>39:
    v=v-40
    print('Сорок ',end='')
elif 40>v>29:
    v=v-30
    print('Тридцать ',end='')
elif 30>v>19:
    v=v-20
    print('Двадцать',end='')
if v==19:
    print('Девятнадцать')
elif v==18:
    print('Восемнадцать')
elif v==17:
    print('Семнадцать')
elif v==16:
    print('Шестнадцать')
elif v==15:
    print('Пятнадцать')
elif v==14:
    print('Четырнадцать')
elif v==13:
    print('Тринадцать')
elif v==12:
    print('Двенадцать')
elif v==11:
    print('Одинадцать')
elif v==10:
    print('Десять')
elif v==9:
    print('Девять')
elif v==8:
    print('Восемь')
elif v==7:
    print('Семь')
elif v==6:
    print('Шесть')
elif v==5:
    print('Пять')
elif v==4:
    print('Четыре')
elif v==3:
    print('Три')
elif v==2:
    print('Два')
elif v==1:
    print('Один')
# Конец модуля 4
#Модуль 5
jear=int(input('Введите год: '))
if jear<1:
    print('К такому меня жизнь не готовила...')
if jear ==1:
    print('Год Чёрной курицы')
elif jear==2:
    print('год чёрной собаки')
elif jear==3:
    print('год чёрной свиньи')
else:
    print('Год ', end='')
    jear=jear-4
    jear=jear%60
    r=jear//12
    if r==0:
        print('зелён',end='')
    elif r==1:
        print('Красн',end='')
    elif r==2:
        print('жёлт',end='')
    elif r==3:
        print('бел',end='')
    else:
        print('чёрн',end='')
    l=jear%12
    if l==0:
        print('ой Крысы')
    elif l==1:
        print('ой Коровы')
    elif l==2:
        print('ого Тигра')
    elif l==3:
        print('ого Зайца')
    elif l==4:
        print('ого Дракона')
    elif l==5:
        print('ой Змеи')
    elif l==6:
        print('ой Лошади')
    elif l==7:
        print('ой Овцы')
    elif l==8:
        print('ой Обезьяны')
    elif l==9:
        print('ой Курицы')
    elif l==10:
        print('ой Собаки')
    elif l==11:
        print('ой Свиньи')
