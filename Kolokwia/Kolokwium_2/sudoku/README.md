```python 
# sprawdza, czy tablica składa się z samych jedynek
def allOnes(a):
    for n in a:
        if n != 1:
            return False
    return True


# Sprawdza czy w każdej kolumnie i wierszu są elementy zgodne z zasadami.
# Nie muszę sprawdzać wewnątrz kwadratów, bo treść zadania zakłada że wejście
# ma je poprawne, a ja nie zmieniam nic w ich wnętrzach.
def isValid(a):
    for i in range(9):
        cnts1 = [0] * 9  # liczba wystąpień każdej cyfry w a[i][*]
        cnts2 = [0] * 9  #                               w a[*][i]
        for j in range(9):
            cnts1[a[i][j] - 1] += 1
            cnts2[a[j][i] - 1] += 1
        if not (allOnes(cnts1) and allOnes(cnts2)):
            return False
    return True


# zamienia podkwadraty o indeksach a i b miejscami
# a, b  w  [0;8] (indeksowane od zera)
def swap(T, a, b):
    # pozycje lewych górnych wierzchołków każdego podkwadratu
    ax, bx = (a % 3) * 3, (b % 3) * 3
    ay, by = (a // 3) * 3, (b // 3) * 3
    for x in range(3):
        for y in range(3):
            T[ax + x][ay + y], T[bx + x][by + y] = T[bx + x][by + y], T[ax + x][ay + y]


def sudoku(T):
    # sprawdzamy każdą parę
    # 9 po 2 = 36 iteracji
    for a in range(9):
        for b in range(a + 1, 9):
            swap(T, a, b)
            r = isValid(T)
            swap(T, a, b)  # przywracamy oryginalną tablicę
            # w szczególności w przypadku gdy znaleźliśmy
            # rozwiązanie - zadanie nie pozwala na modyfikacje
            if r:
                return (a + 1, b + 1)  # zadanie indeksuje podkwadraty od 1
    return None  # niemożliwe dla poprawnych danych wejściowych

```
