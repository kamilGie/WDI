# ====================================================================================================>
# Zadanie 51
# Dane są dwie liczby naturalne z których budujemy trzecią liczbę. W budowanej licz-
# bie muszą wystąpić wszystkie cyfry występujące w liczbach wejściowych. Wzajemna kolejność cyfr każ-
# dej z liczb wejściowych musi być zachowana. Na przykład mając liczby 123 i 75 możemy zbudować liczby
# 12375,17523,75123,17253, itd. Proszę napisać funkcję która wyznaczy `ile` liczb pierwszych można zbudować
# z dwóch zadanych liczb.
# ====================================================================================================>
# return int( ilosci znalezionych tych liczb w)


from math import sqrt


def czy_pierwsza(n):
    if n == 2 or n == 3:
        return True
    elif n <= 1 or n % 2 == 0 or n % 3 == 0:
        return False
    else:
        i = 5
        while i < sqrt(n) + 1:
            if n % i == 0:
                return False
            i += 2
            if n % i == 0:
                return False
            i += 4
    return True


def check_mask(mask, a):
    licznik_jedynek = 0
    while mask > 0:
        if mask % 2 == 1:
            licznik_jedynek += 1

        mask = mask // 2
    return licznik_jedynek == len(str(a))


def nowa_liczba(a, b, mask):
    liczba = 0
    counter = 0
    num_of_digits = len(str(a)) + len(str(b))

    while counter != num_of_digits:
        if mask % 2 == 0:
            liczba += (b % 10) * (10**counter)
            b = b // 10
            mask = mask // 2
            counter += 1
        else:
            liczba += (a % 10) * (10**counter)
            a = a // 10
            mask = mask // 2
            counter += 1
    # end while
    return liczba


def Zadanie_51(a, b):
    length = len(str(a)) + len(str(b))

    ilosci = 0
    for mask in range(1, 2**length):
        if check_mask(mask, a):
            k = nowa_liczba(a, b, mask)
            if czy_pierwsza(k):
                ilosci += 1
    return ilosci


