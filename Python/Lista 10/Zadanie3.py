def pierwsze(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


nieparzyste = [x for x in range(1, 101) if pierwsze(x) and x % 2 != 0]
print("Nieparzyste liczby pierwsze od 1 do 100:", nieparzyste)
