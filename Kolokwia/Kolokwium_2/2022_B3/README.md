<picture>
  <source srcset="../../srt/zbior_zadan/2022_B3.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_2022_B3.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_2022_B3.png" alt="zadanie 2022_B3">
</picture>

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