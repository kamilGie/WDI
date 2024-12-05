<picture>
  <source srcset="../../srt/zbior_zadan/127.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_127.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_127.png" alt="zadanie 127">
</picture>

```python
def multi(T):
    najdluzszy_cykl = 0
    for napis in T:
        n = len(napis)

        # Przeszukiwanie od połowy długości napisu w dół
        for dlugosc_cyklu in range(n // 2, 0, -1):
            # Sprawdzenie, czy długość napisu jest podzielna przez dlugosci_cyklu
            if n % dlugosc_cyklu == 0:
                # Sprawdzenie, czy podnapis o długości `dlugosc_cyklu` powtarzany `liczba_powtorzen` razy tworzy oryginalny napis
                fragment = napis[:dlugosc_cyklu]
                liczba_powtorzen = n // dlugosc_cyklu
                if fragment * liczba_powtorzen == napis:
                    najdluzszy_cykl = max(najdluzszy_cykl, dlugosc_cyklu)
                    break
    return najdluzszy_cykl
```
