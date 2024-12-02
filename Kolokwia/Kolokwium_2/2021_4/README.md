<img width="792" alt="Zrzut ekranu 2024-12-2 o 01 27 42" src="https://github.com/user-attachments/assets/0ef295f4-3921-46b9-935b-29f760a7dbea">

```python
# https://github.com/MarcinSerafin03/bit-algo-start-24-25-WDI/tree/main


def fibo(T):
    a, b = 1, 1
    while a < T[0] or b < T[1]:
        a, b = b, a + b
    if a != T[0]:
        return False

    for i in range(1, len(T)):
        a, b = b, a + b
        if a != T[i]:
            return False
    return True


def Zadanie_4(T):
    maxi = 0
    for i in range(len(T)):
        for j in range(len(T[i]) - 2):
            if fibo(T[i][j : j + 3]):
                curr = 3
                a, b = T[i][j + 1], T[i][j + 2]
                for k in range(j + 3, len(T[i]) - 2):
                    if a + b == T[i][j + 3]:
                        curr += 1
                    else:
                        maxi = max(curr, maxi)
                maxi = max(curr, maxi)
    for j in range(len(T[0])):
        for i in range(len(T) - 2):
            column_slice = [T[i][j], T[i + 1][j], T[i + 2][j]]
            if fibo(column_slice):
                curr = 3
                a, b = T[i + 1][j], T[i + 2][j]
                for k in range(i + 3, len(T)):
                    if a + b == T[k][j]:
                        curr += 1
                        a, b = b, a + b
                    else:
                        break
                maxi = max(curr, maxi)

    return maxi

```