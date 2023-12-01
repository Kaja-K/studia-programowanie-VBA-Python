a = int(input("Podaj pierwsza liczbe: "))
b = int(input("Podaj druga liczbe: "))

if a > b:
    print(f"Liczba {a} jest wieksza")
elif b > a:
    print(f"Liczba {b} jest wieksza")
else:
    print(f"Liczby {a} i {b} są sobie równe")
