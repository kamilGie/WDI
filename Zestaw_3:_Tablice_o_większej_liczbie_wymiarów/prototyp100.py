# ====================================================================================================>
# Zadanie 100
# Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
# w poszukuje w tablicy kwadratu o liczbie pól będącej liczbą nieparzystą większą od 1, którego iloczyn 4 pól
# narożnych wynosi k. Do funkcji należy przekazać tablicę i wartość k. Funkcja powinna zwrócić informacje
# czy udało się znaleźć kwadrat oraz współrzędne (wiersz, kolumna) środka kwadratu.
# ====================================================================================================>

# z wiki ale nie moge jeszcez wymyslec do tego testow


def Zadanie_100(T, k):
    n = len(T)

    for y in range(n):
        for x in range(n):
            bok = 2
            iloczyn = 1
            while y + bok < n and x + bok < n:
                iloczyn = T[y][x] * T[y + bok][x] * T[y][x + bok] * T[y + bok][x + bok]

                if iloczyn == k:
                    return (y + y + bok) // 2, (x + x + bok) // 2
                # end if
                bok += 2
            # end while
    # end for y
    return False


if __name__ == "__main__":
    from Develop import stworz_zadanie

    stworz_zadanie([Zadanie_100])
