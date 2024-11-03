# ====================================================================================================>
# Zadanie 52
# Liczba Smitha to taka, której suma cyfr jest równa sumie cyfr wszystkich liczb występujących
# w jej rozkładzie na czynniki pierwsze. Na przykład: 85=5∗17, 8+5=5+1+7. Proszę napisać program
# wypisujący liczby Smitha mniejsze od 10^6.
# ====================================================================================================>
# print(liczba_smitha)
# i tak dla wszystkich do miliona

# rozwiazanie z wiki ale za malo optymalne
from math import sqrt


def czy_pierwsza(n):
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0 or n % 3 == 0:
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
        # end while
    return True


def suma_cyfr(n):
    suma = 0
    while n > 0:
        suma += n % 10
        n = n // 10

    return suma


def suma_rozkladu(n):
    suma = 0
    i = 2
    if czy_pierwsza(n):
        return suma_cyfr(n) + 1
    else:
        while n != 1:
            while n % i == 0:
                k = suma_cyfr(i)
                suma += k
                n //= i
            # end while
            i += 1
        # end while

    return suma


def Zadanie_52():
    for i in range(1000000):
        if suma_rozkladu(i) == suma_cyfr(i):
            print(i)


if __name__ == "__main__":
    from Develop import stworz_zadanie

    Zadanie_52()
    # stworz_zadanie([Zadanie_52])
