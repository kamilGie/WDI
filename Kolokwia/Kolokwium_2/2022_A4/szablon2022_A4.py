# ====================================================================================================>
# Zadanie A4, 20.12.2022
# Na szachownicy o rozmiarach N × N reprezentowanej przez tablicę T[N][N] umieszczono pewną liczbę
# skoczków. Położenie skoczka w tablicy oznaczono liczbą 1, puste pola oznaczono liczbą 0. Część pustych pól
# na szachownicy jest szachowana przez znajdujące się na niej skoczki. Proszę zaproponować funkcję place(T),
# która znajdzie na szachownicy puste pole położone najbliżej środka szachownicy, takie że umieszczenie tam
# skoczka maksymalnie zwiększy liczbę szachowanych pustych pól. Do funkcji przekazujemy tablicę T zawierającą położenie skoczków.
# Funkcja powinna zwrócić pole (wiersz, kolumna), na którym należy umieścić
# skoczka. Odległość pomiędzy polami: (w1, k1) i (w2, k2) jest równa max(abs(w1 − w2), abs(k1 − k2))
# ====================================================================================================>


def place(T): ...


if __name__ == "__main__":
    from testy2022_A4 import odpal_testy

    place(int(input('Podaj T: ')))

    # odpal_testy()
