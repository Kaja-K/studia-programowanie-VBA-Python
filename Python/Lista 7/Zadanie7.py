a = int(input("Podaj pierwszy bok: "))
b = int(input("Podaj drugi bok: "))
c = int(input("Podaj trzeci bok: "))

if a < b + c and b < a + c and c < a + b:
    wstawka = ""
else:
    wstawka = "nie "

print(f"Z podnaych bokow {wstawka}da sie utworzyc trojkata")
