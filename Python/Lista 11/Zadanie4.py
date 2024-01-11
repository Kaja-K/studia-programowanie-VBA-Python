def polacz_listy(*listy):
    polaczona_lista = []
    for lista in listy:
        polaczona_lista.extend(lista)
    return list(set(polaczona_lista))


lista1 = [1, 2, 3]
lista2 = [3, 4, 5]
lista3 = [5, 6, 7]
wynik = polacz_listy(lista1, lista2, lista3)
print("Połączona lista bez duplikatów:", wynik)
