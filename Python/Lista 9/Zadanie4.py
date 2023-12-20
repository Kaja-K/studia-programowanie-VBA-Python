<<<<<<< HEAD
lista = [
    int(input("Podaj liczbe: "))
    for _ in range(int(input("Ile chcesz wprowadzic liczb? ")))
]

n = int(input("Szukana suma: "))

for i in range(len(lista)):
    for j in range(i, len(lista)):
        if lista[i] + lista[j] == n:
            print(f"{lista[i]} + {lista[j]} = {n}")
=======
lista = [
    int(input("Podaj liczbe: "))
    for _ in range(int(input("Ile chcesz wprowadzic liczb? ")))
]

n = int(input("Szukana suma: "))

for i in range(len(lista)):
    for j in range(i, len(lista)):
        if lista[i] + lista[j] == n:
            print(f"{lista[i]} + {lista[j]} = {n}")
>>>>>>> 36a94e2be9c4aa2f89c8b02892697dc42398bf8b
