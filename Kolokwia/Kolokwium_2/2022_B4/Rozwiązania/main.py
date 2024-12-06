# ====================================================================================================>
# Zadanie B4, 15.12.2022
# Na szachownicy o rozmiarach N × N reprezentowanej przez tablicę T[N][N] umieszczono pewną liczbę
# wież szachowych tak, że każde z wolnych pól na szachownicy jest szachowane. Położenie wież w tablicy
# oznaczono wartościami T rue. Przyszedł zły człowiek i zmienił położenie jednej z wież na szachownicy, tak że
# nie wszystkie wolne pola są szachowane. Proszę zaproponować funkcję move(T), która znajdzie przeniesienie
# jednej wieży, tak aby ponownie wszystkie pola były szachowane. Do funkcji przekazujemy
# tablicę T zawierającą położenie wież po zmianie położenia wieży. Funkcja powinna zwrócić dwa pola (wiersz, kolumna) –
# skąd i dokąd należy przenieść wieżę.
#  ====================================================================================================>


# Brutal force, ale działa – najprościej


def wszystkie_szachowane(T):
    """Sprawdza, czy wszystkie pola na szachownicy T są szachowane."""
    # Tworzę tablicę szachowania przechowującą, czy pole jest szachowane.
    N = len(T)
    szachowane = []
    for i in range(N):
        szachowane.append([False] * N)

    # Sprawdź, które pola są szachowane przez wieże.
    for i in range(N):
        for j in range(N):
            if T[i][j]:  # Jeśli jest wieża w tym miejscu.
                for k in range(N):
                    szachowane[i][k] = True  # Cały wiersz.
                    szachowane[k][j] = True  # Cała kolumna.

    # Sprawdź, czy wszystkie pola są szachowane.
    for i in range(N):
        for j in range(N):
            if not szachowane[i][j]:  # Jeśli pole nie jest szachowane.
                return False
    return True


def move(T):
    N = len(T)
    # Szukamy wież, aby je przestawić.
    for i in range(N):
        for j in range(N):
            if T[i][j]:  # Znalaziono wieżę.
                T[i][j] = False
                # Dla każdego pola sprawdzam, czy przeniesienie jej tam daje wszedzie szach
                for k in range(N):
                    for z in range(N):
                        if not T[k][z]:
                            T[k][z] = True
                            if wszystkie_szachowane(T):
                                return ((i, j), (k, z))
                            T[k][z] = False
                T[i][j] = True
    return
