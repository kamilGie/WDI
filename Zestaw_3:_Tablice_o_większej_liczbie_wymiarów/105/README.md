![Zadanie 105](../../srt/zbior_zadan/105.png)
```python
def compare(a, b):
    cnt = 0
    while a != 0:
        cnt += a % 2
        a = a // 2

    while b != 0:
        cnt -= b % 2
        b = b // 2

    return cnt == 0


def Zadanie_105(T1, T2):
    n, m = len(T1), len(T2)  # n < m
    cnt = 0

    for y in range(m - n + 1):
        for x in range(m - n + 1):
            cnt = 0
            for a in range(n):
                for b in range(n):
                    if compare(T1[a][b], T2[y + a][x + b]):
                        cnt += 1

            if cnt / (n * n) > 0.33:
                print(y, x)
                return True
    return False



```