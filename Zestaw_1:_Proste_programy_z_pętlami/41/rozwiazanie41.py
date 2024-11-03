# ====================================================================================================>
# Zadanie 41
# Napisać program, który wyznacza ostatnia niezerową cyfrę liczby N!. Program powinien
# działać dla N rzędu 10100. Komentarz: Rozwiązanie tego zadania w języku Python jest proste, trochę więk-
# szym wyzwaniem jest rozwiązanie w języku C/C++
# ====================================================================================================>


from math import factorial


def Zadanie_41(N):
    silnia, d = divmod(factorial(N), 10)
    while d == 0:
        silnia, d = divmod(silnia, 10)

    return d


