# ====================================================================================================>
# Zadanie 100
# Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
# w poszukuje w tablicy kwadratu o liczbie pól będącej liczbą nieparzystą większą od 1, którego iloczyn 4 pól
# narożnych wynosi k. Do funkcji należy przekazać tablicę i wartość k. Funkcja powinna zwrócić informacje
# czy udało się znaleźć kwadrat oraz współrzędne (wiersz, kolumna) środka kwadratu.
# ====================================================================================================>
# return False jak nie ma return tuple(wiersz,kolumna) jak istnieje


def Zadanie_100(T, k): ...


if __name__ == "__main__":
    from testy100 import odpal_testy

    Zadanie_100(int(input('Podaj T: ')), int(input('Podaj k: ')))

    # odpal_testy()
