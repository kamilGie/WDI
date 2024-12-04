<picture>
  <source srcset="../../srt/zbior_zadan/124.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_124.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_124.png" alt="zadanie 124">
</picture>

```python
from math import inf

def Zadanie_124(Struktura):
    # Obliczanie najbliższego punktu od osi współrzędnych
    najblizszy_osi = inf
    for x, y in Struktura:
        odleglosc = max(abs(x), abs(y))  # Maksymalna odległość od osi dla tego punktu
        if  odleglosc < najblizszy_osi:
            najblizszy_osi = odleglosc

    # Jeśli najbliższy punkt do osi to (0, 0), zwracamy False
    if najblizszy_osi == 0:
        return False

    # Sprawdzanie obecności czterech wymaganych punktów w strukturze
    prawa_gora = (najblizszy_osi, najblizszy_osi)
    prawa_dol = (najblizszy_osi, -najblizszy_osi)
    lewa_gora = (-najblizszy_osi, najblizszy_osi)
    lewa_dol = (-najblizszy_osi, -najblizszy_osi)

    # Sprawdzamy, czy wszystkie punkty są obecne w strukturze
    return ( prawa_gora in Struktura and prawa_dol in Struktura and lewa_gora in Struktura and lewa_dol in Struktura)
```
