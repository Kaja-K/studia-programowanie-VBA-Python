import math

r = int(input("Podaj promien kola: "))
if r < 0:
    print("promien nie moze byc ujemny")
else:
    print("Pole kola: {}\nObwod kola: {}".format(r**2 * math.pi, 2 * r * math.pi))
