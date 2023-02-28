def q0():
    a = int(input())
    if a >= 36:
        print("плацкарт")
    else:
        print("купе")
    if a%2 == 0:
        print("верх")
    else:
        print("низ")

def q1():
    a = int(input())
    if a%4 == 0 and a%100 != 0 or a%400 == 0:
        print("високосный")
    else:
        print("обычный")

def q2():
    a = ("красный","жёлтый","синий")
    b = input()
    c = input()
    if b in a and c in a:
        if b!= c:
            if b in ("красный","синий") and c in ("красный", "синий"):
                print("фиолетовый")
            if b in ("красный","жёлтый") and c in ("красный", "жёлтый"):
                print("оранжевый")
            if b in ("жёлтый","синий") and c in ("жёлтый", "синий"):
                print("зелёный")
        else:
            print(b)
    else:
        print("ошибка цвета")

def q3():
    n = int(input())
    q = []
    for i in range (n):
        q.append(input())

    print(*q)


q1()
q2()
q3()