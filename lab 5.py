import random

def z1():
    n = []
    for i in range(5):
        n.append(random.randint(1, 10))
    c = int(input("введите число: "))
    if c in n:
        print("да ты гребаный волшебник")
    else:
        print("шестое чувство не твое")
    print(n)

def z2():
    n = []
    for i in range(10):
        n.append(random.randint(1, 10))
    print(*filter(lambda x: n.count(x) > 1, n))

def z3():
    week = ("пн", "вт", "ср", "чт", "пт", "сб", "вс")
    n = int(input("скок чиллить дней хочешь? "))
    if n == 0:
        print("без чилла(")
        print("пахать: ", *week)
    else:
        print("чилл: ", *week[-n:])
        print("пахать: ", *week[:-n])

def z4():
    s_1 = ['Кан', 'Кран', 'Канкан', 'Клан']
    s_2 = ['Кар', 'Как', 'Кек', 'Кек']
    s = tuple(s_1 + s_2)
    print("первый список: ", *s_1)
    print("второй список: ", *s_2)
    print("новый кортеж: ", *sorted(s))
    print("длина кортежа: ", len(s))
    print(s.count('Кан'))
z4()