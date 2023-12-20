<<<<<<< HEAD
zdanie = input("Podaj zdanie: ")
znaki = {}

for znak in zdanie:
    if znak != " ":
        if znak in znaki:
            znaki[znak] += 1
        else:
            znaki[znak] = 1

print("Wystąpienia poszczególnych znaków (bez spacji):")
for znak in znaki:
    print(f"{znak}: {znaki[znak]}")
=======
zdanie = input("Podaj zdanie: ")
znaki = {}

for znak in zdanie:
    if znak != " ":
        if znak in znaki:
            znaki[znak] += 1
        else:
            znaki[znak] = 1

print("Wystąpienia poszczególnych znaków (bez spacji):")
for znak in znaki:
    print(f"{znak}: {znaki[znak]}")
>>>>>>> 36a94e2be9c4aa2f89c8b02892697dc42398bf8b
