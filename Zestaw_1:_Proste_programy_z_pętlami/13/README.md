<picture>
  <source srcset="../../srt/zbior_zadan/13.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_13.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_13.png" alt="zadanie 13">
</picture>

```python
def dzielniki(n):
    i = 2
    suma = 1
    while i * i < n:
        if n % i == 0:
            suma += i + (n // i)
        i += 1

    if i * i == n:
        suma += i

    return suma


def Zadanie_13():
    for i in range(1, 1000001):
        if i == dzielniki(i):
            print(i, end=" ")



```