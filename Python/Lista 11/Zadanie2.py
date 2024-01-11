def wczytaj_plik():
    try:
        nazwa_pliku = input("Podaj nazwę pliku do wczytania: ")
        with open(nazwa_pliku, "r") as plik:
            zawartosc = plik.read()
            return zawartosc
    except FileNotFoundError:
        print("Podany plik nie istnieje.")


print(wczytaj_plik())
