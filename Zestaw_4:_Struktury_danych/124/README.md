![Zadanie 124](../../srt/zbior_zadan/124.png)
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