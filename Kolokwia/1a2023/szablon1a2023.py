# 1A.
# Dwie liczby naturalne większe od 1 są zgodne jeżeli dzielą się przez te same
# liczby pierwsze.  Przykładem zgodnych liczb są pary:
#     (6, 24), (40, 50), (13, 169), (44, 242)
# nie są zgodne np. pary:
#     (6, 8), (40, 60), (13, 39), (44, 99)
#
# Tablica T została wypełniona liczbami z zakresu [2..999]. Sąsiadami pola o
# indeksie i w tablicy są pola o indeksie j, gdy abs(i-j) < 3.
# Proszę napisać funkcję zgodne(T), która dla tak wypełnionej tablicy zwraca
# liczbę elementów mających przynajmniej jednego zgodnego sąsiada. Po wykonaniu
# funkcji tablica nie musi pozostać nie zmieniona.
# Na przykład dla tablicy:  T = [2, 3, 4, 5, 7, 6, 23, 24, 12, 13, 14, 15, 16, 45]
# funkcja powinna zwrócić wartość 7 (są to liczby 2, 4, 6, 24, 12, 15, 45).


def zgodne(T: list[int]): ...


if __name__ == "__main__":
    from testy1a2023 import odpal_testy

    # odpal_testy()
