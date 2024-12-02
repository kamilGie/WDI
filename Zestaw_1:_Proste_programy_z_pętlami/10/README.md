![Zadanie 10](../../srt/zbior_zadan/10.png)
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