<picture>
  <source srcset="../../srt/zbior_zadan/124.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_124.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_124.png" alt="zadanie 124">
</picture>

```python
def Zadanie_124(Struktura):
    najblizszy_osi = min(max(abs(x), abs(y)) for x, y in Struktura)
    return (
        najblizszy_osi != 0
        and (najblizszy_osi, najblizszy_osi) in Struktura
        and (najblizszy_osi, -najblizszy_osi) in Struktura
        and (-najblizszy_osi, najblizszy_osi) in Struktura
        and (-najblizszy_osi, -najblizszy_osi) in Struktura
    )

```