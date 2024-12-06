# ====================================================================================================>
# Zadanie B4, 15.12.2022
# Na szachownicy o rozmiarach N × N reprezentowanej przez tablicę T[N][N] umieszczono pewną liczbę
# wież szachowych tak, że każde z wolnych pól na szachownicy jest szachowane. Położenie wież w tablicy
# oznaczono wartościami True. Przyszedł zły człowiek i zmienił położenie jednej z wież na szachownicy, tak że
# nie wszystkie wolne pola są szachowane. Proszę zaproponować funkcję move(T), która znajdzie przeniesienie
# jednej wieży, tak aby ponownie wszystkie pola były szachowane. Do funkcji przekazujemy
# tablicę T zawierającą położenie wież po zmianie położenia wieży. Funkcja powinna zwrócić dwa pola (wiersz, kolumna) –
# skąd i dokąd należy przenieść wieżę.
#  ====================================================================================================>
# To zadanie zazwyczaj ma wiele poprawnych rozwiązań, więc na testy patrzyłbym z przymrużeniem oka.


def move(T): ...


if __name__ == "__main__":
    from testy2022_B4 import odpal_testy

    move(
        [
            [True, True, False],
            [False, True, False],
            [False, False, False],
        ]
    )  # return  ((0, 0), (2, 0))

    # odpal_testy()
