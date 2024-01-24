# zadnie 1
def dzielniki(num):
    dzielniki = [1]
    for i in range(2, num + 1):
        if num % i == 0:
            dzielniki.append(i)
    return dzielniki


try:
    num = int(input(("podaj liczbe całkowita: ")))
except:
    print("bład danych")

if num < 0:
    print("błędne dane")
else:
    if len(dzielniki(num)) == 2:
        print("liczba jest pierwsza")
    else:
        print("dzielniki ", dzielniki(num))

# liczba pierwsza - ma dwa różne dzielniki 1 i samą siebie

# zadanie 2
slowo = ""
tab = []

while True:
    slowo = input("podaj całkowitą: ")
    if slowo == "end":
        break
    try:
        tab.append(int(slowo))
    except:
        print("bład danych")


print("suma: ", sum(tab), " zawartość: ", tab)
