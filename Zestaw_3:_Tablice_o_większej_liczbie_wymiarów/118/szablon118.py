# ====================================================================================================>
# Zadanie 118
# Dana jest tablica T[N][N] (reprezentująca szachownicę) wypełniona liczbami naturalnymi.
# W każdej kolumnie znajduje się dokładnie jedna wieża, której numer wiersza zawiera tablica int w[N].
# Proszę napisać funkcję która wybiera do usunięcia z szachownicy dwie wieże, tak aby suma liczb na polach
# szachowanych przez pozostałe wieże była najmniejsza. Do funkcji należy przekazać tablice t i w, funkcja
# powinna zwrócić numery kolumn z których usunięto wieże. Uwaga - zakładamy, że wieża szachuje cały
# wiersz i kolumnę z wyłączeniem pola na którym stoi
# ====================================================================================================>


def Zadanie_118(T, w) -> tuple: ...


if __name__ == "__main__":
    from testy118 import odpal_testy

    Zadanie_118(int(input("Podaj T: ")), int(input("Podaj w: ")))

    # odpal_testy()
