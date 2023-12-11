dict = {
    "zarzadzanie": "W8",
    "inzynieria zarzadzania": "W8",
    "informatyka techniczna": "W4",
    "architektura": "W1",
    "fizyka techniczna": "W11",
}

kierunek_uzytkownika = input("Podaj kierunek: ")

if kierunek_uzytkownika in dict:
    print(
        f"Kierunek {kierunek_uzytkownika} znajduje się na Wydziale {dict[kierunek_uzytkownika]}"
    )
else:
    print(f"Przepraszamy, kierunek {kierunek_uzytkownika} nie jest oferowany na PWr.")
