# ====================================================================================================>
# Zadanie 102
# Dwie liczby naturalne są „przyjaciółkami jeżeli zbiory cyfr z których zbudowane są liczby
# są identyczne. Na przykład: 123 i 321, 211 i 122, 35 3553. Dana jest tablica T[N][N] wypełniona liczbami
# naturalnymi. Proszę napisać funkcję, która dla tablicy T zwraca ile elementów tablicy sąsiaduje wyłącznie z
# przyjaciółkami
# ====================================================================================================>


def same_digits(a, b):
    T1 = [0] * 10
    T2 = [0] * 10

    while a > 0:
        T1[a % 10] = 1
        a = a // 10
    # end while

    while b > 0:
        T2[b % 10] = 1
        b = b // 10
    # end while

    return T1 == T2


# end def


def is_on_board(T, y, x):
    if 0 <= y < len(T):
        if 0 <= x < len(T):
            return True
    # end if
    return False


# end def is_on_board


def Zadanie_102(T):
    cnt = 0
    n = len(T)

    for y in range(n):
        for x in range(n):
            flag = True
            jumps = [
                (-1, -1),
                (-1, 0),
                (-1, 1),
                (0, 1),
                (1, 1),
                (1, 0),
                (1, -1),
                (0, -1),
            ]
            for ele in jumps:
                if is_on_board(T, y + ele[0], x + ele[1]):
                    if not same_digits(T[y][x], T[y + ele[0]][x + ele[1]]):
                        flag = False
                        break
                    # end if 2
                # end if 1
            # end for x
            if flag == True:
                cnt += 1
    # end for y

    return cnt


# end def zad11


