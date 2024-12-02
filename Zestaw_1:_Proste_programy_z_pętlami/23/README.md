![Zadanie 23](../../srt/zbior_zadan/23.png)
```python
from math import sqrt


def average(a, b):
    while abs(a - b) > 0.000001:
        a, b = sqrt(a * b), (a + b) / 2
    # end while
    return (a + b) / 2



```