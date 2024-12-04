<picture>
  <source srcset="../../srt/zbior_zadan/68.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_68.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_68.png" alt="zadanie 68">
</picture>

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