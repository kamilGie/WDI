# ====================================================================================================>
# Zadanie 107
# Dana jest tablica T[N][N], wypełniona liczbami naturalnymi. Proszę napisać funkcję która
# odpowiada na pytanie, czy w tablicy każdy wiersz zawiera co najmniej jedną liczbą złożoną wyłącznie z cyfr
# będących liczbami pierwszymi?
# ====================================================================================================>
# return bool


def same_cyfry_pierwsze(n):
    k = n
    primes = {2, 3, 5, 7}
    while k > 0:
        if (k % 10) not in primes:
            return False
        k = k // 10
    # end while
    return True


def Zadanie_107(tab):
    n = len(tab)

    for y in range(n):
        flag = False
        for x in range(n):

            if same_cyfry_pierwsze(tab[y][x]):
                flag = True
                break
            # end if

        # end for 2
        if not flag:
            return False

    # end for 1
    return True


