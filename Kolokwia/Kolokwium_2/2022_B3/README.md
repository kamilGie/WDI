![black_Zrzut ekranu 2024-12-6 o 11 18 04](https://github.com/user-attachments/assets/76d72d65-7a41-4ab7-b668-5ec346a1d5c0)

```python
from math import inf


def rook(N, L):
    def legalne(x, y):
        return (0 <= x < N) and (0 <= y < N)

    def ruch(pos, prev_move=None):
        """zwroci minimalna ilosci ruchow lub inf jak sie nie da dotrzec z danej pozycji do mety"""
        if not legalne(pos[0], pos[1]):  # wyszlismy po za szachownice
            return inf
        if pos in L:  # pozycja pionka
            return inf
        if pos == (N - 1, N - 1):  # meta
            return 0

        # sprawdzam 2 mozliwosci ruchu z danej pozycji
        prawo = ruch((pos[0], pos[1] + 1), "prawo")
        dol = ruch((pos[0] + 1, pos[1]), "dol")

        # jesli skrecilem dodaj to do ruchow
        if prev_move != "prawo":
            prawo += 1
        if prev_move != "dol":
            dol += 1

        # zwracam najmniejsza mozliwosci
        return min(dol, prawo)

    res = ruch((0, 0))
    return None if res == inf else res
```
