from random import randint

x = randint(1, 100)

proby = 0
while True:
    zgadnij = int(input("Podaj liczbe: "))
    proby += 1
    if zgadnij > x:
        print("Szukana wartosc jest mniejsza.")
    elif zgadnij < x:
        print("Szukana wartosc jest wieksza.")
    else:
        print(f"Gratulacje! Zgadles po {proby} probach.")
        break
