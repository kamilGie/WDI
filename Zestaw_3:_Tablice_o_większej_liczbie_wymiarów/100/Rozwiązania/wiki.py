# ====================================================================================================>
# Zadanie 100
# Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
# w poszukuje w tablicy kwadratu o liczbie pól będącej liczbą nieparzystą większą od 1, którego iloczyn 4 pól
# narożnych wynosi k. Do funkcji należy przekazać tablicę i wartość k. Funkcja powinna zwrócić informacje
# czy udało się znaleźć kwadrat oraz współrzędne (wiersz, kolumna) środka kwadratu.
# ====================================================================================================>
# return False jak nie ma return tuple(wiersz,kolumna) jak istnieje


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
                bok += 2
    return False


