<picture>
  <source srcset="../../srt/zbior_zadan/10.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_10.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_10.png" alt="zadanie 10">
</picture>

```python
def Zadanie_10(liczba):
    if liczba < 2:
        return False
    else:
        dzielnik = 2
        while dzielnik**2 <= liczba:
            if liczba % dzielnik == 0:
                return False
            dzielnik += 1
        return True

```