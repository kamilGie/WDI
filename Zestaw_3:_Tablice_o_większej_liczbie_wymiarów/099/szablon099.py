# ====================================================================================================>
# Zadanie 99
# Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
# w poszukuje w tablicy najdłuższego ciągu geometrycznego leżącego ukośnie w kierunku prawo-dół, liczącego
# co najmniej 3 elementy. Do funkcji należy przekazać tablicę. Funkcja powinna zwrócić informacje czy udało
# się znaleźć taki ciąg oraz długość tego ciągu.
# ====================================================================================================>
# return false jak nie ma
# return dlugosci jak istnieje
# geometric_series([[1, 3, 9], [2, 6, 18], [4, 12, 36]]) -> return  3


def geometric_series(T): ...


if __name__ == "__main__":
    from testy099 import odpal_testy

    geometric_series(list(input("Podaj T: ")))

    # odpal_testy()
