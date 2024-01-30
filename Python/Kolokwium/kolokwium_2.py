def suma(x, y):
    lista = []
    for i in range(x, y + 1):
        if i % 2 != 0:
            lista.append(i)
    return sum(lista)


try:
    x = int(input("podaj x: "))
    y = int(input("podaj y: "))
    if x < y:
        nx = x
        ny = y
    else:
        nx = y
        ny = x
    print(suma(nx, ny))
except ValueError:
    print("error")


def kelwin(lista):
    new_lista = []
    for i in range(len(lista)):
        new_lista.append(lista[i] + 273.15)
    return new_lista


lista = []
i = 0
while True:
    try:
        x = float(input("podaj tem w celcjuszach: "))
        lista.append(x)
        if i == 4:
            break
        else:
            i += 1
    except ValueError:
        print("error")

print(kelwin(lista))
