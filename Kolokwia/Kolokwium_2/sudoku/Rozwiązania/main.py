def isValid(a):
    """sprawdzam czy jakas liczba nie wystapila 2 razy w wierszu lub kolumnie"""
    for i in range(9):
        appear_row, appear_col = [False] * 10, [False] * 10 # 10 aby miec liczby 1-9 z niepotrzebnym 0
        for j in range(9):
            # liczba juz wystapila mamy powtorzenie
            if appear_row[a[i][j]] or appear_col[a[j][i]]:
                return False

            # dodaje do tablicy wystapien liczbe
            appear_row[a[i][j]] = appear_col[a[j][i]] = True

    return True


def swap(T, a, b):
    """ zamienia podkwadraty o indeksach a i b miejscami """
    # pozycje lewych górnych wierzchołków każdego podkwadratu
    ax, ay = a[0], a[1]
    bx, by = b[0], b[1]
    subgrid_offsets = [ (0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2) ]
    for x, y in subgrid_offsets:
        T[ax + x][ay + y], T[bx + x][by + y] = T[bx + x][by + y], T[ax + x][ay + y]


def sudoku(T):
    # pozycje lewych górnych wierzchołków każdego podkwadratu
    subgrid_top_left_positions = [ (0, 0), (3, 0), (6, 0), (0, 3), (3, 3), (6, 3), (0, 6), (3, 6), (6, 6) ]

    # sprawdzamy każdą parę
    for a in range(9):
        for b in range(a + 1, 9):
            swap(T, subgrid_top_left_positions[a], subgrid_top_left_positions[b])
            r = isValid(T)
            swap(T, subgrid_top_left_positions[a], subgrid_top_left_positions[b])
            # przywracamy oryginalną tablicę
            if r:
                return (a + 1, b + 1)  # zadanie indeksuje podkwadraty od 1
    return None  # niemożliwe dla poprawnych danych wejściowych
