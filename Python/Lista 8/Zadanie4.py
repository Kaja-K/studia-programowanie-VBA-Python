k = int(input("Podaj liczbe k: "))
print(*[i for i in range(50, 101) if i % k == 0])
