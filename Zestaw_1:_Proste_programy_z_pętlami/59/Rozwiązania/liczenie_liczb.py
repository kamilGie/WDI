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


def liczenie_liczb():
    def count_digits(sorted_numbers):
        count = [0] * 10
        current_digit = -1
        digit_count = 0

        for number in sorted_numbers:
            if number != current_digit:
                if current_digit != -1:
                    count[current_digit] = digit_count
                current_digit = number
                digit_count = 1
            else:
                digit_count += 1

        if current_digit != -1:
            count[current_digit] = digit_count

        return count

    print("2", "3", "5", "7", end=" ")
    znalezione = 4
    dlugosci = 2
    potegi = [d for d in range(10)]

    while True:

        potegi = [d * potegi[d] for d in range(10)]

        for kombinacje in combinations_with_replacement(range(10), dlugosci):

            suma_cyfr = sum(kombinacje)
            if suma_cyfr % 2 == 0 or suma_cyfr % 3 == 0:
                continue

            s = sum(potegi[d] for d in kombinacje)
            if s % 2 == 0 or s % 5 == 0 or s % 7 == 0 or s % 11 == 0 or s % 13 == 0:
                continue

            lista_wystapien = count_digits((kombinacje))
            tmp = s
            while tmp:
                tmp, d = divmod(tmp, 10)
                if lista_wystapien[d] == 0:
                    break
                lista_wystapien[d] -= 1
            else:
                if not any(lista_wystapien) and isprime(s):
                    print(s, end=" ")
                    znalezione += 1
                    if znalezione == 7:
                        print()
                        return

        dlugosci += 1
