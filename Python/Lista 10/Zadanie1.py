def KC(kelv):
    if kelv < 0:
        return None
    else:
        return round(kelv - 273.15, 2)


temp = int(input("Podaj temperature w kelwinach "))
print(f"{temp}K to {KC(temp)}°C")
