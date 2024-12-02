![Zadanie 099](../../srt/zbior_zadan/099.png)
```python
def geometric_series(T):
    max_leng = 1

    for x in range(len(T) - 2):
        q = T[1][x + 1] / T[0][x]
        leng = 2

        for i in range(2, len(T) - x):  # i - wiersze

            if T[i][x + i] == T[i - 1][x + i - 1] * q:
                leng += 1

            else:
                max_leng = max(max_leng, leng)
                q = T[i][x + i] / T[i - 1][x + i - 1]

        max_leng = max(max_leng, leng)
    # end for 1

    for y in range(len(T) - 2):
        q = T[y + 1][1] / T[y][0]
        leng = 2

        for i in range(2, len(T) - y):

            if T[y + i][i] == T[y + i - 1][i - 1] * q:
                leng += 1

            else:
                max_leng = max(max_leng, leng)
                leng = 2
                q = T[y + i][i] / T[y + i - 1][i - 1]
        max_leng = max(max_leng, leng)
    # end for 2
    return max_leng if max_leng >= 3 else False



```