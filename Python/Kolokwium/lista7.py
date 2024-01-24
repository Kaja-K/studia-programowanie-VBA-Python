# 1
imie = input("Podaj imie: ")

try:
    rok = int(input("Podaj rok urodzenia: "))
except:
    print("złe dane")

print(imie, "masz ", 2024 - rok, "lat")

# 2
try:
    a = int(input("podaj a: "))
    b = int(input("podaj b: "))

    print("suma: ", a + b)
    print("różnica: ", a - b)
    print("iloraz: ", a / b)
    print("pierwiastek sumy: ", (a + b) ** (1 / 2))
    print("a do potegi b: ", a**b)
    print("b do potegi a: ", b**a)

except:
    print("złe dane")

# 3
try:
    r = int(input("podaj promien: "))
    if r < 0:
        print("promien nie moze byc ujemny")
    else:
        print("Pole kola: ", 3.14 * r**2)
        print("Obwod kola: ", 2 * 3.14 * r)
except:
    print("złe dane")

# 4
try:
    a = int(input("podaj a: "))
    b = int(input("podaj b: "))
    if a > b:
        print("liczba a jest wieksza od b")
    elif b > a:
        print("liczba b jest wieksza od a")
    else:
        print("Liczby sa rowne")
except:
    print("złe dane")

# 5
imie = input("Podaj imie: ")
try:
    rok = int(input("Podaj rok urodzenia: "))
    if 2024 - rok > 17:
        pelnoletni = ", jestes pelnoletni"
    else:
        pelnoletni = ", nie jestes pelnoletni"
    print(imie, "masz ", 2024 - rok, "lat", pelnoletni)
except:
    print("złe dane")

# 6
print("Podaj trzy boki trojkata: ")
try:
    a = int(input("podaj a: "))
    b = int(input("podaj b: "))
    c = int(input("podaj c: "))
    if a + b > c and a + c > b and b + c > a:
        print("z podanych bokow mozna stworzyc trojkat")
    else:
        print("z podanych nie bokow mozna stworzyc trojkata")
except:
    print("zle dane")

# 7
try:
    pkt = int(input("Podaj punkty: "))
    if pkt < 50:
        s, l = "ndst", 2
    elif pkt >= 50 and pkt < 60:
        s, l = "dst", 3
    elif pkt >= 60 and pkt < 70:
        s, l = "dst+", 3.5
    elif pkt >= 70 and pkt < 80:
        s, l = "db", 4
    elif pkt >= 80 and pkt < 90:
        s, l = "db+", 4.5
    elif pkt >= 50 and pkt < 60:
        s, l = "bdb", 5
    else:
        s, l = "cel", 5.5
    wybor = str(input("Podaj opcje oceny(slownie/liczbowo/oba): "))
    if wybor == "slownie":
        print(s)
    elif wybor == "liczbowo":
        print(l)
    else:
        print(s, l)
except:
    print("zle dane")
