# ====================================================================================================>
# Zadanie 150
# Dane są dwie liczby naturalne z których budujemy trzecią liczbę. W budowanej liczbie
# muszą wystąpić wszystkie cyfry występujące w liczbach wejściowych. Wzajemna kolejność cyfr każdej z liczb
# wejściowych musi być zachowana. Na przykład mając liczby 123 i 75 możemy zbudować liczby 12375,17523,
# 75123, 17253, itd. Proszę napisać funkcję która wyznaczy ile liczb pierwszych można zbudować z dwóch
# zadanych liczb.
# ====================================================================================================>


from math import sqrt


def prime(n):
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i < sqrt(n) + 1:
        if n % i == 0:
            return False
        i += 2
        if n % i == 0:
            return False
        i += 4
    # end
    return True


###


def new_number_prime(a, b):

    def rek(a, b, x, i):
        if a == 0 and b == 0:
            if prime(x):
                print(x)
                return 1
            return 0
        if a == 0:
            return rek(a, 0, x + b * (10**i), i + 1)
        if b == 0:
            return rek(0, b, x + a * (10**i), i + 1)
        return rek(a // 10, b, x + (a % 10) * (10**i), i + 1) + rek(
            a, b // 10, x + (b % 10) * (10**i), i + 1
        )

    return rek(a, b, 0, 0)


