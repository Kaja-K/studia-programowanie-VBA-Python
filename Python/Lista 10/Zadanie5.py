def dodawanie(w1, w2):
    return [a + b for a, b in zip(w1, w2)]


def odejmowanie(w1, w2):
    return [a - b for a, b in zip(w1, w2)]


def mnozenie(w1, w2):
    result = [0] * (len(w1) + len(w2) - 1)
    for i in range(len(w1)):
        for j in range(len(w2)):
            result[i + j] += w1[i] * w2[j]
    return result


# BEZ UŻYCIA FUNCKJI ZIP

# def dodawanie(w1, w2):
#     result = []
#     for i in range(min(len(w1), len(w2))):
#         result.append(w1[i] + w2[i])
#     if len(w1) > len(w2):
#         result.extend(w1[len(w2) :])
#     elif len(w1) < len(w2):
#         result.extend(w2[len(w1) :])
#     return result


# def odejmowanie(w1, w2):
#     result = []
#     for i in range(min(len(w1), len(w2))):
#         result.append(w1[i] - w2[i])
#     if len(w1) > len(w2):
#         result.extend(w1[len(w2) :])
#     elif len(w1) < len(w2):
#         result.extend([-x for x in w2[len(w1) :]])
#     return result

w1 = [2, -3, 0, 4]
w2 = [1, 5, 2]

print("Wynik dodawania:", dodawanie(w1, w2))
print("Wynik odejmowania:", odejmowanie(w1, w2))
print("Wynik mnozenia:", mnozenie(w1, w2))
