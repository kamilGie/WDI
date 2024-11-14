# ====================================================================================================>
# Zadanie 122
# Na szachownicy o wymiarach 100 na 100 umieszczamy N hetmanów (N <100). Położenie
# hetmanów jest opisywane przez tablicę dane=[(w1 ,k1 ),(w2 ,k2 ),(w3 ,k3 ),...(wn ,kn )] Proszę napisać funk-
# cję, która odpowiada na pytanie: czy żadne z dwa hetmany się nie szachują? Do funkcji należy przekazać
# położenie hetmanów.
# ====================================================================================================>
# return bool


def Zadanie_122(tab):
    for y in range(len(tab)):
        for x in range(y + 1, len(tab)):
            w1, k1 = tab[y]
            w2, k2 = tab[x]

            if w1 == w2 or k1 == k2:
                return False

            quotient = (w2 - w1) / (k2 - k1)
            if quotient == -1.00 or quotient == 1.00:
                return False

    return True


