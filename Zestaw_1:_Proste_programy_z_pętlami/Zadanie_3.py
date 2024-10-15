# ====================================================================================================>
# Zadanie 3
# Proszę znaleźć wyrazy początkowe ciągu zamiast 1,1 o najmniejszej sumie, aby w ciągu
# analogicznym do ciągu Fibonacciego wystąpił wyraz równy numerowi bieżącego roku.
# ====================================================================================================>


def Zadanie_3():
    suma = 10000
    best = (0, 0)
    for i in range(1, 2023):
        x = i
        y = 2024

        while x > 0 and y > x:
            x, y = y - x, x

        if x + y < suma:
            best = (x, y)
            suma = x + y
    print(suma, best)


Zadanie_3()
