![Zadanie 152](../../srt/zbior_zadan/152.png)
```python
def get_first_digit(num):
    while num > 9:
        num //= 10

    return num


def Zadanie_152(board: list, x, y):

    def rek(x, y, b: list, been=set()):
        been.add((x, y))

        if (
            x == 7
            and y == 7
            or x == 0
            and y == 7
            or x == 0
            and y == 0
            or x == 7
            and y == 0
        ):
            return True

        for x_n, y_n in (
            (x, y + 1),
            (x + 1, y + 1),
            (x + 1, y),
            (x + 1, y - 1),
            (x, y - 1),
            (x - 1, y - 1),
            (x - 1, y),
            (x - 1, y + 1),
        ):
            try:
                if not (x_n, y_n) in been:
                    cand = get_first_digit(b[y_n][x_n])
                    if cand > b[y][x] % 10:
                        if rek(x_n, y_n, b, been):
                            return True
            except IndexError:
                pass

        return False

    return rek(x, y, board)



```