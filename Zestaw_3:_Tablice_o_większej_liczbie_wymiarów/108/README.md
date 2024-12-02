<picture>
  <source srcset="../../srt/zbior_zadan/108.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_108.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_108.png" alt="zadanie 108">
</picture>

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