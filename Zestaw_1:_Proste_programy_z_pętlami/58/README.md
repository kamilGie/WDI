<picture>
  <source srcset="../../srt/zbior_zadan/58.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_58.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_58.png" alt="zadanie 58">
</picture>

```python
from itertools import combinations_with_replacement

N = 15


def Zadanie_58():
    ilosci_zer = len(str(10**N))
    for dlugosci in range(ilosci_zer):
        for kombinacje in combinations_with_replacement(range(10), dlugosci):
            suma = sum(liczba**dlugosci for liczba in kombinacje)

            if list(kombinacje) == sorted(int(ch) for ch in str(suma)):
                print(suma)



```