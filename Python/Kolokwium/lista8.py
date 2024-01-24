# 1
liczby = []
while True:
    try:
        liczba = input("podaj liczby: ")
        if liczba != "end":
            liczby.append(int(liczba))
        else:
            break
    except:
        print("error")

try:
    print(sum(liczby) / len(liczby))
except:
    print("error")

# 2
try:
    a = int(input("podaj a: "))

    for i in range(0, a):
        print(i)
except:
    print("blad")

# 3
try:
    a = int(input("podaj a: "))
    b = int(input("podaj b: "))

    if a > b:
        wa = b
        wb = a
    else:
        wa = a
        wb = b

    for i in range(wa, wb + 1):
        print(i)
except:
    print("blad")

# 4
i = 50

try:
    k = int(input("podaj k: "))

    while i != 100:
        if i % k == 0:
            print(i)
        i += 1
except:
    print("blad danych")

# 5
liczba = 69
while True:
    try:
        x = int(input("podaj szukana: "))
        if liczba > x:
            print("szukana jest wieksza")
        elif liczba < x:
            print("szuakana jest mniejsza")
        else:
            print("brawo zgadles")
            break
    except:
        print("blad danych")

# 6
for i in range(10):
    print("*  " * 10)

# 7
for i in range(1, 4):
    for j in range(i + 1, 5):
        for k in range(j + 1, 6):
            print(i, j, k)
