# ile = int(input("Ile chcesz wprowadzic liczb? "))
# lista1 = [0] * ile
# for i in range(ile):
#     lista1[i] = int(input(f"Podaj liczbe {i+1}: "))
# print(f"Maksymalna liczba wynosi: : {max(lista1)}, a minimalna: {min(lista1)}")


lista2 = [
    int(input("Podaj liczbe: "))
    for _ in range(int(input("Ile chcesz wprowadzic liczb? ")))
]
print(f"Maksymalna liczba wynosi: : {max(lista2)}, a minimalna: {min(lista2)}")
