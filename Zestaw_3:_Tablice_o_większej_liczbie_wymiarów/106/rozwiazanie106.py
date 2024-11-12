# ====================================================================================================>
# Zadanie 106
# Dana jest tablica T[N][N], wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
# odpowiada na pytanie, czy w tablicy istnieje wiersz, w którym każda liczba zawiera co najmniej jedną cyfrę
# będącą liczbą pierwszą?
# ====================================================================================================>
# return bool


def czy_zawiera(n):
    k = n
    primes = {2, 3, 5, 7}

    while k > 0:
        if (k % 10) in primes:
            return True
        k = k // 10
    # end while
    return False


def Zadanie_106(tab):
    n = len(tab)

    for y in range(n):
        flag = True
        for x in range(n):
            if not czy_zawiera(tab[y][x]):
                flag = False
                break
        # end for 2
        if flag:
            return True
        flag = True
    # end for 1
    return False


