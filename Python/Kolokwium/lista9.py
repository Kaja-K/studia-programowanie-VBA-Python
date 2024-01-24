# 1
n = int(input("podaj ile chcesz liczb: "))

lista = []
while True:
    try:
        if len(lista) == n:
            break
        else:
            liczba = int(input("podaj liczbe: "))
            lista.append(liczba)
    except:
        print("error")

print(lista)

# 2
print(sum(lista))

# 3
print(min(lista), max(lista))

# 4
try:
    s = int(input("szukana suma: "))
    for i in range(len(lista)):
        for j in range(i, len(lista)):
            if lista[i] + lista[j] == s:
                print(lista[i], "+", lista[j], " = ", s)
except:
    print("error")

# 5
dict = {
    "zarzadzanie": "W8",
    "inzynieria zarzadzania": "W8",
    "informatyka techniczna": "W4",
    "architektura": "W1",
    "fizyka techniczna": "W11",
}


kierunek = str(input("podaj kierunek: "))

if kierunek in dict:
    print(dict.get(kierunek))
else:
    print("error")

# 6
zdanie = str(input("podaj zdanie: "))
znaki = {}

# for znak in zdanie:
#     if znak != " ":
#         if znak in znaki:
#             znaki[znak] += 1
#         else:
#             znaki[znak] = 1

# print(znaki)

for znak in zdanie:
    if znak != " ":
        if znak in znaki:
            continue
        else:
            znaki[znak] = zdanie.count(znak)
print(znaki)
