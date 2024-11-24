# ====================================================================================================>
# Zadanie 118
# Dana jest tablica T[N][N] (reprezentująca szachownicę) wypełniona liczbami naturalnymi.
# W każdej kolumnie znajduje się dokładnie jedna wieża, której numer wiersza zawiera tablica int w[N].
# Proszę napisać funkcję która wybiera do usunięcia z szachownicy dwie wieże, tak aby suma liczb na polach
# szachowanych przez pozostałe wieże była najmniejsza. Do funkcji należy przekazać tablice t i w, funkcja
# powinna zwrócić numery kolumn z których usunięto wieże. Uwaga - zakładamy, że wieża szachuje cały
# wiersz i kolumnę z wyłączeniem pola na którym stoi
# ====================================================================================================>


def Zadanie_118(T, w):
    """
    Wystarczy tylko sprawdzać przecięcia wież. Są to jedyne pola, które po usunięciu wież przestaną być szachowane.
    Należy więc znaleźć maksymalną sumę tych dwóch przecięć.
    """

    n = len(w)
    res = (0, 0)
    max_nie_szachowanych = 0
    for w1 in range(n):
        for w2 in range(w1 + 1, n):
            nie_szachowane = T[w[w1]][w2] + T[w[w2]][w1]
            if nie_szachowane > max_nie_szachowanych:
                max_nie_szachowanych = nie_szachowane
                res = (w1, w2)

    return res
