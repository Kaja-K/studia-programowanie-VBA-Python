numbers = []

while (value := input("Podaj liczbe lub wpisz 'end' aby zakonczyc: ")) != "end":
    try:
        numbers.append(float(value))
    except ValueError:
        print("Blad: Nieprawidlowy format liczby.")

if not numbers:
    print("Blad: Brak danych.")
else:
    average = sum(numbers) / len(numbers)
    print(f"Srednia arytmetyczna: {average}")
