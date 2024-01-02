def doskonala(number):
    dziel = sum([i for i in range(1, number) if number % i == 0])
    return dziel == number


# def doskonala(number):
#     dzielniki = []
#     for i in range(1, number):
#         if number % i == 0:
#             dzielniki.append(i)

#     suma_dzielnikow = sum(dzielniki)
#     return suma_dzielnikow == number


n = int(input("Podaj liczbe "))
if doskonala(n):
    print(f"{n} to liczba doskonala")
else:
    print(f"{n} nie jest liczba doskonala")
