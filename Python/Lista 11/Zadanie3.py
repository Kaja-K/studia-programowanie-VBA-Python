def sprawdz_wystapienia_slowa(plik, slowo):
    with open(plik, "r") as file:
        tekst = file.read()
        ilosc_wystapien = tekst.lower().count(slowo.lower())
        print(f"Słowo '{slowo}' wystąpiło {ilosc_wystapien} razy w pliku tekst.txt.")


sprawdz_wystapienia_slowa("Lista 11/tekst.txt", "kot")
