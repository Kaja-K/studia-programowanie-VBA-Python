import random

lista_elementow = [3, 5, 8, 1, 4, 9, 10, 2, 3, 4]

print("Losowy element z listy:", random.choice(lista_elementow))
print("Losowo wybrane elementy z powoórzeniami:", random.choices(lista_elementow, k=3))
