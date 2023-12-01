punkty = int(input("Podaj liczbe punktow: "))

if 0 <= punkty < 50:
    ocena, slownie = 2.0, "dostateczny"
elif 50 <= punkty < 60:
    ocena, slownie = 3.0, "dopuszczajacy"
elif 60 <= punkty < 70:
    ocena, slownie = 3.5, "dopuszczajacy z plusem"
elif 70 <= punkty < 80:
    ocena, slownie = 4.0, "dobry"
elif 80 <= punkty < 90:
    ocena, slownie = 4.5, "dobry z plusem"
elif 90 <= punkty < 100:
    ocena, slownie = 5.0, "bardzo dobry"
elif punkty == 100:
    ocena, slownie = 5.5, "bardzo dobry z plusem"
else:
    print("Błędna liczba punktów")
    exit()

wybor = input("Podaj forme oceny (liczbowo/slownie/oba): ")

if wybor == "liczbowo":
    print(ocena)
elif wybor == "oba":
    print(f"{ocena} {slownie}")
else:
    print(slownie)

"""oceny = [(2.0, "ndst"),(2.5, "ndst+"),(3.0, "dst"),(3.5, "dst+"),(4.0, "db"),(4.5, "db+"),(5.0, "bdb"),(5.5, "bdb+"),]
punkty = max(int(input("Podaj liczbe punktow: ")) - 30, 0)
wybor = input("Podaj forme oceny (liczbowo/slownie/oba): ")
ocena = oceny[int(punkty // 10)]
if wybor == "liczbowo":print(ocena[0])
elif wybor == "oba":print(f"{ocena[0]} {ocena[1]}")
else:print(ocena[1])"""
