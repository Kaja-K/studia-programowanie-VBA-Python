# 1
def k_to_c(k):
    if k > 0:
        return k - 270
    else:
        return "k nie moze byc mniejsze od 0"


# try:
#     print(k_to_c(int(input("podaj liczbe: "))))
# except:
#     print("bledne dane")


# 2
def dzielniki(n):
    lista = []
    for i in range(1, n):
        if n % i == 0:
            lista.append(i)
    return lista


def doskonala(n):
    if n == sum(dzielniki(n)):
        return " liczba jest doskonala"
    else:
        return " liczba nie jest doskonala"


# try:
#     print(doskonala(int(input("podaj liczbe: "))))
# except:
#     print("bledne dane")


# 3
def generuj():
    lista = []
    for i in range(1, 100):
        if len(dzielniki(i)) < 3 and i % 2 != 0:
            lista.append(i)
    return lista


# print(generuj())


def silnia(n):
    if n == 0:
        return 1
    else:
        return n * silnia(n - 1)


# try:
#     print(silnia(int(input("podaj liczbe: "))))
# except:
#     print("bledne dane")
