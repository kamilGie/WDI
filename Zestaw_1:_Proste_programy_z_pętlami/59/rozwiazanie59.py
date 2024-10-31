# ====================================================================================================>
# Zadanie 59
# Tylko 7 liczb pierwszych spełnia warunek z poprzedniego zadania. Proszę napisać program
# znajdujący wszystkie te liczby.
# ====================================================================================================>
# zwrocic print(liczba) wiec 7 takich printow

# napisanie tego bez tablic bedzie bardziej bardzo drobiazgowe kiedys zrobie
# te liczby to 2, 3, 5, 7, 28116440335967, 449177399146038697307, 35452590104031691935943,

from itertools import combinations_with_replacement
from sympy import isprime


# def isprime(n):
#     i = 5
#     while i * i <= n:
#         if n % i == 0 or n % (i + 2) == 0:
#             return False
#         i += 6
#     return True


def Zadanie_59():
    print("2", "3", "5", "7", sep="\n")
    znalezione = 4
    dlugosci = 2
    potegi = [d for d in range(10)]

    while True:

        potegi = [d * potegi[d] for d in range(10)]

        for kombinacje in combinations_with_replacement(range(10), dlugosci):

            print("dlugosci: ", dlugosci)
            if dlugosci == 21:
                return

            suma_cyfr = sum(kombinacje)
            if suma_cyfr % 2 == 0 or suma_cyfr % 3 == 0:
                continue

            s = sum(potegi[d] for d in kombinacje)
            if s % 2 == 0 or s % 5 == 0 or s % 7 == 0 or s % 11 == 0 or s % 13 == 0:
                continue

            temp = s
            sumdigits = []
            while temp:
                temp, d = divmod(temp, 10)
                sumdigits.append(d)

            if list(kombinacje) == sorted(sumdigits) and isprime(s):
                print(s)
                znalezione += 1
                if znalezione == 7:
                    return

        dlugosci += 1


