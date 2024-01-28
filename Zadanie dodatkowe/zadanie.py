slownik = {}


def wyswietl_slownik():
    print("Lista studentów:")
    if not slownik:
        print("Brak studentów.")
    else:
        for student, ocena in slownik.items():
            print(f"{student} - {ocena}")


def dodaj_do_slownika():
    try:
        imie_nazwisko = input("Podaj imię i nazwisko studenta:\n>")
        ocena = float(input("Podaj ocenę:\n>"))

        while not (0 <= ocena <= 5):
            print("Nieprawidłowa ocena. Podaj ocenę od 0 do 5.")
            ocena = float(input(">"))

        slownik[imie_nazwisko] = ocena
        print("Dodano studenta.")
    except ValueError:
        print("Błąd wartości")


def usun_ze_slownika():
    imie_nazwisko = input("Podaj imię i nazwisko studenta do usunięcia:\n>")
    if imie_nazwisko in slownik:
        del slownik[imie_nazwisko]
        print("Usunięto studenta.")
    else:
        print("Nie znaleziono studenta o podanym imieniu i nazwisku.")


def znajdz_i_wyswietl_klucz():
    imie_nazwisko = input("Podaj imię i nazwisko studenta do znalezienia:\n>")
    if imie_nazwisko in slownik:
        print(f"{imie_nazwisko} - {slownik[imie_nazwisko]}")
    else:
        print("Nie znaleziono studenta o podanym imieniu i nazwisku.")


def znajdz_i_wyswietl_klucze_po_wartosci():
    try:
        ocena = float(input("Podaj ocenę do wyszukania studentów:\n>"))
        znalezione = []

        for student, wartosc in slownik.items():
            if wartosc == ocena:
                znalezione.append(student)

        if znalezione:
            print(f"Studenci o ocenie {ocena}:")
            for student in znalezione:
                print(student)
        else:
            print("Nie znaleziono studentów o podanej ocenie.")

    except ValueError:
        print("Błąd wartości")


while True:
    print("\nWitaj w systemie obsługi studentów. Dostępne opcje:")
    print("1. Pokaż listę studentów")
    print("2. Dodaj studenta z oceną")
    print("3. Usuń studenta")
    print("4. Znajdź studenta")
    print("5. Znajdź studentów po ocenie")
    print("6. Zakończ działanie")

    wybor = input(">")

    if wybor == "1":
        wyswietl_slownik()
    elif wybor == "2":
        dodaj_do_slownika()
    elif wybor == "3":
        usun_ze_slownika()
    elif wybor == "4":
        znajdz_i_wyswietl_klucz()
    elif wybor == "5":
        znajdz_i_wyswietl_klucze_po_wartosci()
    elif wybor == "6":
        break
    else:
        print("Nieprawidłowy wybór. Wybierz ponownie.")
