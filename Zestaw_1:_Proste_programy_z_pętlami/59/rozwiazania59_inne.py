# ====================================================================================================>
# Zadanie 59
# Tylko 7 liczb pierwszych spełnia warunek z poprzedniego zadania. Proszę napisać program
# znajdujący wszystkie te liczby.
# ====================================================================================================>
# zwrocic od spacji te liczby 2 3 5 7 28116440335967 449177399146038697307 35452590104031691935943


# test Millera-Rabina sprawdzajacy czy liczba jest pierwsza.
# Mozna tez napisac jakis deterministyczny test.
# lecz dla liczb narcystycznych test Millera-Rabina dziala z wielkim prawdopodobeistwiem


import random


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


# Rozne rozwiazania:


# W teorii szybciej byłoby napisać własną implementację tego.
# Jednak import ten jest zaimplementowana w C.
# Więc niezależnie od tego, co by się wymyśliło, importowanie będzie szybsze.
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


def porownywanie_stringiem():
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

            cyfry_sumy = sorted((map(int, str(s))))
            for kom, c_sum in zip(kombinacje, cyfry_sumy):
                if kom != c_sum:
                    break
            else:
                if isprime(s):
                    print(s, end=" ")
                    znalezione += 1
                    if znalezione == 7:
                        print()
                        return

        dlugosci += 1


def bez_tablic():
    print("2", "3", "5", "7", end=" ")
    znalezione = 4
    dlugosci = 2
    potegi = list(range(0, 10))
    mnoznik = range(0, 10)

    while True:
        potegi = list(map(lambda p, m: p * m, potegi, mnoznik))

        for kombinacje in combinations_with_replacement(range(10), dlugosci):
            suma_cyfr = sum(kombinacje)
            if suma_cyfr % 2 == 0 or suma_cyfr % 3 == 0:
                continue

            s = 0
            iterator = iter(potegi)
            potega = next(iterator)
            wartosci_iteratora = 0
            for d in kombinacje:
                if wartosci_iteratora != d:
                    for _ in range(d - wartosci_iteratora):
                        wartosci_iteratora += 1
                        potega = next(iterator)
                s += potega

            if s % 2 == 0 or s % 5 == 0 or s % 7 == 0 or s % 11 == 0 or s % 13 == 0:
                continue

            cyfry_sumy = sorted((map(int, str(s))))
            for kom, c_sum in zip(kombinacje, cyfry_sumy):
                if kom != c_sum:
                    break
            else:
                if isprime(s):
                    print(s, end=" ")
                    znalezione += 1
                    if znalezione == 7:
                        print()
                        return

        dlugosci += 1


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
                    print(s, end="")
                    znalezione += 1
                    if znalezione == 7:
                        print()
                        return

        dlugosci += 1


# to jest glowne rozwiazanie ale dodalem by byly tutaj wszystkie
def reguly_zestawu_pierwszego():
    import math

    # zeby nie potegowac za kazdym razem potegi bede trzymal w zmiene ktore beda przy kazdym dodaniu dlugosci mnozyc
    P_2 = 2
    P_3 = 3
    P_4 = 4
    P_5 = 5
    P_6 = 6
    P_7 = 7
    P_8 = 8
    P_9 = 9

    def sprawdz_liczbe(licznik_liczb_digita, s):
        # jesli jest podzielna przez te liczby to nawet nie warto isc dalej bo wiemy ze nie jest pierwsza
        if (
            s % 2 == 0
            or s % 3 == 0
            or s % 5 == 0
            or s % 7 == 0
            or s % 11 == 0
            or s % 13 == 0
            # jesli jej dlugosci nie odpowiada dlugosci liczb zer to tez mozemy isc dalej
            or math.floor(math.log10(s)) + 1 != length
        ):
            return False

        # tworzymy w notacj liczacej liczbe sum
        licznik_liczb_sumy = 0
        tmp = s
        while tmp > 0:
            tmp, d = divmod(tmp, 10)
            licznik_liczb_sumy += 100**d

        # sprawdzamy czy liczby w naszej notacji liczacej sa takie same i  s jest pierwsza mamy wynik
        if licznik_liczb_sumy != licznik_liczb_digita or not isprime(s):
            return False

        print(s, end=" ")
        return True

    # tworze kombinacje powtorzen od 0 do 10 dla dlugosci zer i zamist zwracac te dlugosci sprawdzaj
    # ich liczbe wystapien kazdej liczby w notacji |liczba dziewiatek|liczba osemek|i tak dalej do 0|...
    # oraz wynik tych wystapien liczb razy dlugosci ilosci zer jaki mamy
    def kombinacje_powtorzen_dziesiatki(r, start=0, licznik_liczb=0, s=0):
        if r == 0:
            return sprawdz_liczbe(licznik_liczb, s)
        else:
            znalezione = 0
            i = start

            if i == 0:
                znalezione += kombinacje_powtorzen_dziesiatki(
                    r - 1, 0, licznik_liczb + 100**i, s
                )
                i += 1
            if i == 1:
                znalezione += kombinacje_powtorzen_dziesiatki(
                    r - 1, 1, licznik_liczb + 100**i, s + 1
                )
                i += 1
            if i == 2:
                znalezione += kombinacje_powtorzen_dziesiatki(
                    r - 1, 2, licznik_liczb + 100**i, s + P_2
                )
                i += 1
            if i == 3:
                znalezione += kombinacje_powtorzen_dziesiatki(
                    r - 1, 3, licznik_liczb + 100**i, s + P_3
                )
                i += 1
            if i == 4:
                znalezione += kombinacje_powtorzen_dziesiatki(
                    r - 1, 4, licznik_liczb + 100**i, s + P_4
                )
                i += 1
            if i == 5:
                znalezione += kombinacje_powtorzen_dziesiatki(
                    r - 1, 5, licznik_liczb + 100**i, s + P_5
                )
                i += 1
            if i == 6:
                znalezione += kombinacje_powtorzen_dziesiatki(
                    r - 1, 6, licznik_liczb + 100**i, s + P_6
                )
                i += 1
            if i == 7:
                znalezione += kombinacje_powtorzen_dziesiatki(
                    r - 1, 7, licznik_liczb + 100**i, s + P_7
                )
                i += 1
            if i == 8:
                znalezione += kombinacje_powtorzen_dziesiatki(
                    r - 1, 8, licznik_liczb + 100**i, s + P_8
                )
                i += 1
            znalezione += kombinacje_powtorzen_dziesiatki(
                r - 1, 9, licznik_liczb + 100**i, s + P_9
            )

            return znalezione

    length = 1
    print("2", "3", "5", "7", end=" ")
    znalezione = 4
    while znalezione != 7:
        length += 1
        P_2 *= 2
        P_3 *= 3
        P_4 *= 4
        P_5 *= 5
        P_6 *= 6
        P_7 *= 7
        P_8 *= 8
        P_9 *= 9
        znalezione += kombinacje_powtorzen_dziesiatki(length)
    print()


if __name__ == "__main__":
    import time

    start_time = time.time()
    reguly_zestawu_pierwszego()
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Czas reguly zestawu pierwszego: {execution_time} sekund\n")

    start_time = time.time()
    liczenie_liczb()
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Czas liczenie liczb: {execution_time} sekund\n")

    start_time = time.time()
    bez_tablic()
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Czas bez tablic: {execution_time} sekund\n")

    start_time = time.time()
    porownywanie_stringiem()
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Czas porownywanie stringiem: {execution_time} sekund\n")

    start_time = time.time()
    dzieleniePrzez10()
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Czas dzielenie przez 10: {execution_time} sekund\n")
