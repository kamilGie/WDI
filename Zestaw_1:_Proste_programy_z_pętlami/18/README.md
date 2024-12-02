![Zadanie 18](../../srt/zbior_zadan/18.png)
```python
from math import sqrt


def Zadanie_18():

    a1 = sqrt(0.5)
    a2 = sqrt(0.5 + 0.5 * a1)
    iloczyn = a1 * a2

    while abs(a2 - a1) > 0.00000001:
        a1 = a2
        a2 = sqrt(0.5 + 0.5 * a1)
        iloczyn *= a2

    print(2 / iloczyn)



```