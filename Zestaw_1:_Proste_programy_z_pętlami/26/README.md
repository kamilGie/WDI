<picture>
  <source srcset="../../srt/zbior_zadan/26.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_26.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_26.png" alt="zadanie 26">
</picture>

```python
def ulamek(a, b, n):
    print(a // b, end="")
    if a % b != 0:
        print(".", end="")
        a = a % b
        while a > 0 and n > 0:
            a = a * 10
            print(a // b, end="")
            a = a % b
            n = n - 1

```