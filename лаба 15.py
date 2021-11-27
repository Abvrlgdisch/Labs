#Модуль 1
def PowerA3(A):
    B=A**3
    print('Чиселка Бэ равна: ',B)
# Конец модуля 1
# Модуль 2
def Sign(X):
    if X<0:
        a=-1
    elif X==0:
        a=0
    else:
        a=1
    return(a)
# Конец модуля 2
# Модуль 3
def Rings(R1,R2):
    return(R1*3.14-R2*3.14)
# Конец модуля 3
# Модуль 4
def Quarter(x,y):
    if x>0 and y>0:
        return('Первая четверть')
    elif x>0 and y<0:
        return('Вторая четверть')
    elif x<0 and y<0:
        return('Третья четверть')
    elif x<0 and y>0:
        return('Четвёртая четверть')
    elif x==0 and y==0:
        return('Точка в начале координат')
    else:
        return('Точка где-то на оси...')
# Конец модуля 4
# Модуль 5
def Fact2(N):
    m=1
    if N%2==0:
        for i in range(2,N+1,2):
            m=m*i
    else:
        for i in range(1,N+1,2):
            m=m*i
    return(m)
# Конец модуля 5
