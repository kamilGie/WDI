<picture>
  <source srcset="../../srt/zbior_zadan/102.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_102.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_102.png" alt="zadanie 102">
</picture>

```python
def same_digits(a, b):
    T1 = [0] * 10
    T2 = [0] * 10

    while a > 0:
        T1[a % 10] = 1
        a = a // 10

    while b > 0:
        T2[b % 10] = 1
        b = b // 10

    return T1 == T2


def is_on_board(T, y, x):
    if 0 <= y < len(T):
        if 0 <= x < len(T):
            return True
    return False


def Zadanie_102(T):
    cnt = 0
    n = len(T)

    for y in range(n):
        for x in range(n):
            flag = True
            jumps = [
                (-1, -1),
                (-1, 0),
                (-1, 1),
                (0, 1),
                (1, 1),
                (1, 0),
                (1, -1),
                (0, -1),
            ]
            for ele in jumps:
                if is_on_board(T, y + ele[0], x + ele[1]):
                    if not same_digits(T[y][x], T[y + ele[0]][x + ele[1]]):
                        flag = False
                        break
            if flag == True:
                cnt += 1
    return cnt



```