#Модуь 1
N=input('Введите список. Элементы списка разделяйте символом *, иначе магии не случится: ').split('*')
spisok=[]
for i in N:
    spisok.append(int(i))
K=int(input('Введите номер начала: '))
L=int(input('Введите конечный номер: '))
индекс=0
делитель=0
делимое=0
for i in spisok:
    if K<=индекс<=L:
        делимое+=spisok[индекс]
        делитель+=1
        индекс+=1
    else:
        индекс+=1
        continue
print(делимое/делитель)
# Конец модуля 1
# Модуль 2
N=input('Введите список. Элементы списка разделяйте символом *, иначе магии не случится: ').split('*')
spisok=[]
ind=1
Ant=0
for i in N:
    spisok.append(int(i))
d=spisok[1]-spisok[0]
for i in spisok:
    ind+=1
    if ind>=len(spisok):
        break
    if spisok[ind]-spisok[ind-1]!=d:
        print('НУЛЬ!!!')
        Ant=0
        break
    else:
        Ant=1
if Ant==1:
    print('Получите разность прогрессии: ',d)
# Конец модуля 2
# Модуль 3
A=input('Введите список. Элементы списка разделяйте *, иначе кина не будет').split('*')
spisok=[]
spisok2=[]
for i in A:
    spisok.append(int(i))
ind=0
for i in spisok:
    if ind%2!=0:
        ind+=1
        continue
    else:
        spisok2.append(spisok[ind])
        ind+=1
print(min(spisok2))
#Конец модуля 3
#модуль 4
massiv=input('Введите массив. Элементы разделяйте звёздочкой, иначе кина не будет: ').split('*')
massiv2=[]
for i in massiv:
    massiv2.append(int(i))
massiv=[]
for i in massiv2[::-1]:
    massiv.append(i)
a=1
for i in massiv[1:len(massiv)-2:1]:
    if massiv[a-1]<i>massiv[a+1]:
        print('номер элемента последнего локального максимума: ',len(massiv2)-a)
        break
    else:
        a+=1    
# Конец модуля 4
# Модуль 5 (Я хз, почему оно не работает...)
#spisok=input('Введите список. Символы разделяйте звёздочкой, иначе магии не будет: ').split('*')
#spisok2=[]
#for i in spisok:
#    spisok2.append(int(i))
#m=0
#n=1
#print(len(spisok2))
#while spisok2[m]!=spisok2[n]:
#    if n<len(spisok2)-1:
#        n+=1
#        print('Эн равно: ',n)
#    elif n==len(spisok2)-2:
#        m+=1
#        n=m+1
#    else:
#        print('Что-то не так!!!')
#        break
#print('Найдено совпадение. Элементы имеют индексы: ',m,' и ',n)
