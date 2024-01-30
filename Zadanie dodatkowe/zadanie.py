slownik = {}


def wyswietl_slownik():
    # Sprawdzanie, czy słownik nie jest pusty.
    if not slownik:
        print("Brak studentów na liście.")
    else:
        print("Lista studentów:")

        # Wyświetlanie imion i ocen studentów.
        for student, ocena in slownik.items():
            print(f"{student} - {ocena}")


def dodaj_do_slownika():
    try:
        imie_nazwisko = input("Podaj imię i nazwisko studenta:\n>")

        t_n = ""

        # Sprawdzanie, czy student już istnieje w słowniku.
        if imie_nazwisko in slownik:
            print("Czy chcesz nadpisać ocenę? ")
            t_n = input("Wpisz tak lub nie\n>")

            # Sprawdzanie, czy użytkownik chce nadpisać ocenę.
            if t_n != "tak":
                return

        ocena = float(input("Podaj ocenę:\n>"))

        # Sprawdzenie czy ocena mieści się w zakresie od 2 do 5.5.
        while not (2 <= ocena <= 5.5):
            print("Nieprawidłowa ocena. Podaj ocenę od 2 do 5.5.")
            ocena = float(input(">"))

        # Dodawanie nowego studenta do słownika.
        slownik[imie_nazwisko] = ocena

        # Informacja o dodaniu lub zmianie oceny studenta.
        if t_n == "tak":
            print("Zmieniono ocenę")
        else:
            print("Dodano studenta.")

    except ValueError:
        print("Błąd wartości")


def usun_ze_slownika():
    imie_nazwisko = input("Podaj imię i nazwisko studenta do usunięcia:\n>")

    # Sprawdzanie, czy student istnieje w słowniku.
    if imie_nazwisko in slownik:
        # Usuwanie studenta.
        del slownik[imie_nazwisko]
        print("Usunięto studenta.")
    else:
        print("Nie znaleziono studenta o podanym imieniu i nazwisku.")


def znajdz_i_wyswietl_klucz():
    imie_nazwisko = input("Podaj imię i nazwisko studenta do znalezienia:\n>")

    # Sprawdzanie, czy student istnieje w słowniku.
    if imie_nazwisko in slownik:
        print(f"{imie_nazwisko} - {slownik[imie_nazwisko]}")
    else:
        print("Nie znaleziono studenta o podanym imieniu i nazwisku.")


def znajdz_i_wyswietl_klucze_po_wartosci():
    try:
        ocena = float(input("Podaj ocenę do wyszukania studentów:\n>"))
        znalezione = []

        # Poszukiwaniu studentów o danej ocenie.
        for student, wartosc in slownik.items():
            if wartosc == ocena:
                znalezione.append(student)

        # Wyświetlanie znalezionych studentów.
        if znalezione:
            print(f"Studenci o ocenie {ocena}:")
            for student in znalezione:
                print(student)
        else:
            print("Nie znaleziono studentów o podanej ocenie.")

    except ValueError:
        print("Błąd wartości")


# Menu programu.
while True:
    print("\nWitaj w systemie obsługi studentów. Dostępne opcje:")
    print("1. Pokaż listę studentów")
    print("2. Dodaj studenta z oceną")
    print("3. Usuń studenta")
    print("4. Znajdź studenta")
    print("5. Znajdź studentów po ocenie")
    print("6. Zakończ działanie")

    wybor = input(">")

    # Obsługa wyboru użytkownika
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
