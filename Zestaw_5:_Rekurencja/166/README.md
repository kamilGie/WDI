<picture>
  <source srcset="../../srt/zbior_zadan/166.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_166.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_166.png" alt="zadanie 166">
</picture>

```python

# https://github.com/MarcinSerafin03/bit-algo-start-24-25-WDI/blob/main/Zestaw%205/166.py

from math import factorial


def find_reconstruction(T1, T2):
    def recontruct(T, T_check, accumulator):
        nonlocal T_result, cur_index
        n = len(T)

        # warunek końcowy
        flag = False
        for i in range(n):
            if T_check[i]:
                flag = True

        if not flag:
            T_result[cur_index] = accumulator
            cur_index += 1
            return

        # krok rekurencji
        for i in range(n):
            if T_check[i]:
                T_check[i] = False
                recontruct(T, T_check, accumulator + T[i])
                T_check[i] = True

    T_result = ["" for _ in range(factorial(len(T1)))]
    cur_index = 0

    recontruct(T1, [True for _ in range(len(T1))], "")

    T1_result = T_result

    T_result = ["" for _ in range(factorial(len(T2)))]
    cur_index = 0

    recontruct(T2, [True for _ in range(len(T2))], "")

    T2_result = T_result

    potential_result = ""

    for t1 in T1_result:
        for t2 in T2_result:
            if t1 == t2:
                if potential_result == "":
                    potential_result = t1
                # check if its different matching
                elif potential_result != t1 and potential_result != t2:
                    return False

    return potential_result if potential_result != "" else False
```
