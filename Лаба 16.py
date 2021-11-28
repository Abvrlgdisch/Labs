# Модуль 1
N=int(input('Введите нужную длинну массива'))
spisok=[]
for i in range(1,N*2,2):
    spisok+=[i]
print(spisok)
# Конец модуля 1
# Модуль 2
N=int(input('Введите нужную длинну списка: '))
A=int(input('Введите первый член геометрической прогрессии: '))
D=int(input('Введите знаменатель: '))
step=0
spisok2=[]
while len(spisok2)<N:
    spisok2+=[A*D**step]
    step+=1
print(spisok2)
# Конец модуля 2
# Модуль 3
N=int(input('Введите длинну списка: '))
A=int(input('Введите первый член списка'))
B=int(input('Введите второй член списка'))
spisok3=[]
spisok3+=[A]
spisok3+=[B]
spisok3+=[A+B]
step=2
while len(spisok3)<N:
    spisok3+=[(A+B)*step]
    step=step*2
print(spisok3)
# Конец модуля 3
# Модуль 4
A=input().split(',')
B=[]
while len(A)>0:
    print(A[0],'*',end='')
    print(A[-1],'*',end='')
    del A[0]
    del A[-1]
# Конец модуля 4
# Модуль 5
A=input('Введите массив, разделяя элементы запятыми: ').split(',')
b=0
while len(A)>b:
    if b%2==0:
        print(A[b],end='*')
        b+=1
    else:
        b+=1
        continue
b=len(A)-1
while b>-1:
    if b%2!=0:
        print(A[b],end='*')
        b-=1
    else:
        b-=1
        continue
# Конец модуля 5        
    
