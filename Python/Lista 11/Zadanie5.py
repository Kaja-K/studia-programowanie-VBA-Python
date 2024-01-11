def zlicz_unikalne_slowa(plik_wejsciowy, plik_wyjsciowy):
    with open(plik_wejsciowy, "r") as wejscie:
        tekst = wejscie.read()
        slowa = tekst.split()
        slownik_slow = {}
        for slowo in slowa:
            slowo = slowo.lower()
            slownik_slow[slowo] = slownik_slow.get(slowo, 0) + 1

        with open(plik_wyjsciowy, "w") as wyjscie:
            for slowo, ilosc in slownik_slow.items():
                wyjscie.write(f"{slowo}: {ilosc}\n")


zlicz_unikalne_slowa("Lista 11/tekst.txt", "Lista 11/plik_wyjsciowy.txt")
