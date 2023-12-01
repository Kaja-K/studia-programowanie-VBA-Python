imie = input("Podaj swoje imię: ")
rok = int(input("Podaj rok urodzenia: "))
wiek = 2023 - rok

if wiek > 18:
    pelnoletni = "Jestes pelnoletni"
else:
    pelnoletni = "Nie jestes pelnoletni"

print("{}, masz {} lat\n{}".format(imie, wiek, pelnoletni))
