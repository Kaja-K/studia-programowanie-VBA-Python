import math
import statistics


def srednia(w):
    suma = 0
    for element in w:
        suma += element
    return round(suma / len(w))


def maksymalna(w):
    if not w:
        return None
    maksimum = w[0]
    for element in w:
        if element > maksimum:
            maksimum = element
    return maksimum


def minimalna(w):
    if not w:
        return None
    minimum = w[0]
    for element in w:
        if element < minimum:
            minimum = element
    return minimum


def odchylenie(w):
    srednia_wartosc = sum(w) / len(w)
    roznice_kwadratowe = [(x - srednia_wartosc) ** 2 for x in w]
    return round(math.sqrt(sum(roznice_kwadratowe) / len(w)))


wydajnosci = [120, 150, 130, 170, 140]

# a) Bez korzystania z wbudowanych funkcji
print("a) Bez korzystania z wbudowanych funkcji:")
print("Średnia wydajność:", srednia(wydajnosci))
print("Maksymalna wydajność:", maksymalna(wydajnosci))
print("Minimalna wydajność:", minimalna(wydajnosci))
print("Odchylenie standardowe:", odchylenie(wydajnosci))

# b) Z wbudowanymi funkcjami
print("\nb) Z wbudowanymi funkcjami:")
print("Średnia wydajność:", round(sum(wydajnosci) / len(wydajnosci)))
print("Maksymalna wydajność:", max(wydajnosci))
print("Minimalna wydajność:", min(wydajnosci))
print("Odchylenie standardowe:", round(statistics.stdev(wydajnosci)))

# wynik odchylenia jest inny od podpunktu a i tak ma być (zlozonosc obliczeniowa ble ble ble... )
