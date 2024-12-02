![Zadanie 68](../../srt/zbior_zadan/68.png)
```python
def Zadanie_68(T: list):
    max_dlugosci = 1
    akutalna_dlugosci = 1
    ostatnia_wartosic = T[0]
    for liczba in T[1:]:
        if ostatnia_wartosic < liczba:
            akutalna_dlugosci += 1
            if max_dlugosci < akutalna_dlugosci:
                max_dlugosci = akutalna_dlugosci
        else:
            akutalna_dlugosci = 1
        ostatnia_wartosic = liczba
    return max_dlugosci

```