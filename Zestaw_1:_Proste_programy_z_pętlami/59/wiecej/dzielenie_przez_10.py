# ===================================================================================================>
# Zadanie 59
# Tylko 7 liczb pierwszych spełnia warunek z poprzedniego zadania. Proszę napisać program
# znajdujący wszystkie te liczby.
# ====================================================================================================>


import random

# test Millera-Rabina sprawdzajacy czy liczba jest pierwsza.
# Mozna tez napisac jakis deterministyczny test.
# lecz dla liczb narcystycznych test Millera-Rabina dziala z wielkim prawdopodobeistwiem


def pow_mod(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if (exp % 2) == 1:
            result = (result * base) % mod
        exp //= 2
        base = (base * base) % mod
    return result


def isprime(n, k=15):
    d = n - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow_mod(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow_mod(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True


from itertools import combinations_with_replacement


def dzieleniePrzez10():
    print("2", "3", "5", "7", end=" ")
    znalezione = 4
    length = 2
    potegi = [d for d in range(10)]
    while znalezione != 7:
        potegi = [d * potegi[d] for d in range(10)]

        for digits in combinations_with_replacement(range(10), length):

            suma_cyfr = sum(digits)
            if suma_cyfr % 2 == 0 or suma_cyfr % 3 == 0:
                continue

            # robimy sume cyfer razy potega dlugosci liczb kombinacji ktora liczymy
            s = sum(potegi[d] for d in digits)

            # jesli jest podzielne przez 2,5,7,11,13 to nie  jest liczba pierwsza
            if s % 2 == 0 or s % 5 == 0 or s % 7 == 0 or s % 11 == 0 or s % 13 == 0:
                continue

            temp = s
            sumdigits = []
            while temp:
                temp, d = divmod(temp, 10)
                sumdigits.append(d)

            if list(digits) == sorted(sumdigits) and isprime(s):
                print(s, end=" ")
                znalezione += 1
                if znalezione == 7:
                    print()
                    break

        length += 1
