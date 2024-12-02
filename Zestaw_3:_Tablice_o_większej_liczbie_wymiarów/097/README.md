![Zadanie 097](../../srt/zbior_zadan/097.png)
```python
# https://github.com/MarcinSerafin03/bit-algo-start-24-25-WDI/tree/main


def Zadanie_97(T1):
    N = len(T1)
    Indexes_Table = [0 for _ in range(N)]
    T2_index = 0
    T2 = [0 for _ in range(N * N)]

    while True:
        smallest = float("inf")
        is_singleton = False
        for i in range(N):
            if Indexes_Table[i] >= N:
                continue
            if smallest == T1[i][Indexes_Table[i]]:
                is_singleton = False
            elif smallest > T1[i][Indexes_Table[i]]:
                smallest = T1[i][Indexes_Table[i]]
                is_singleton = True

        if is_singleton:
            print(f"found singleton {smallest}")  # debuging purposes
            T2[T2_index] = smallest
            T2_index += 1

        if smallest == float("inf"):
            break

        for i in range(N):
            if Indexes_Table[i] >= N:
                continue
            if smallest == T1[i][Indexes_Table[i]]:
                Indexes_Table[i] += 1

    return T2

```