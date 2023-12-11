# ile = int(input("Ile chcesz wprowadzic liczb? "))
# lista1 = [0] * ile
# for i in range(ile):
#     lista1[i] = input(f"Podaj liczbe {ile}: ")
# print(lista1)


lista2 = [
    int(input("Podaj liczbe: "))
    for _ in range(int(input("Ile chcesz wprowadzic liczb? ")))
]
print(lista2)
