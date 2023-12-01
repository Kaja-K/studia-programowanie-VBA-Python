ksiazki = [1, 2, 3, 4, 5]
ilosc_wyboru = 3

for i in range(len(ksiazki) - 2):
    for j in range(i + 1, len(ksiazki) - 1):
        for k in range(j + 1, len(ksiazki)):
            print(ksiazki[i], ksiazki[j], ksiazki[k])
