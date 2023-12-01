a = int(input("Podaj pierwsza liczbe: "))
b = int(input("Podaj druga liczbe: "))

print(
    "Suma: {}\nRóżnica: {}\nIloczyn: {}\nIloraz: {}\nPierwiastek sumy: {}\nPotega a: {}\nPotega b: {}".format(
        a + b,
        a - b,
        a * b,
        a / b,
        (a + b) ** 0.5,
        a**b,
        b**a,
    )
)
