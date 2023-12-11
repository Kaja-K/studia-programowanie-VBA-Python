# ile = int(input("Ile chcesz wprowadzic liczb? "))
# lista1 = [0] * ile
# for i in range(ile):
#     lista1[i] = int(input(f"Podaj liczbe {i+1}: "))
# print(f"Suma podanych liczb wynosi: {sum(lista1)}")

lista2 = [
    int(input("Podaj liczbe: "))
    for _ in range(int(input("Ile chcesz wprowadzic liczb? ")))
]
print(f"Suma podanych liczb wynosi: {sum(lista2)}")

# # bez funkcji sum
# suma = 0
# ile = int(input("Ile chcesz wprowadzic liczb? "))
# lista3 = [0] * ile
# for i in range(ile):
#     lista3[i] = int(input(f"Podaj liczbe {i+1}: "))
#     suma += lista3[i]
# print(f"Suma podanych liczb wynosi: {suma}")
