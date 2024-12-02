![Zadanie 108](../../srt/zbior_zadan/108.png)
```python
def Zadanie_108(T):
    n = len(T)
    max_sum = -1
    result = (-1, -1)

    for i in range(n):
        for j in range(n):
            current_sum = 0

            if i > 0:
                current_sum += T[i - 1][j]
            if i < n - 1:
                current_sum += T[i + 1][j]
            if j > 0:
                current_sum += T[i][j - 1]
            if j < n - 1:
                current_sum += T[i][j + 1]
            if i > 0 and j > 0:
                current_sum += T[i - 1][j - 1]
            if i > 0 and j < n - 1:
                current_sum += T[i - 1][j + 1]
            if i < n - 1 and j > 0:
                current_sum += T[i + 1][j - 1]
            if i < n - 1 and j < n - 1:
                current_sum += T[i + 1][j + 1]

            if current_sum > max_sum:
                max_sum = current_sum
                result = (i, j)

    return result



```