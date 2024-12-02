<picture>
  <source srcset="../../srt/zbior_zadan/140.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_140.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_140.png" alt="zadanie 140">
</picture>

```python
def waga(
    li, n, p=0
):  # li - lista odważników, n - szukana waga, p - numer branego odważnika
    if n == 0:
        return True
    if p == len(li):
        return False
    return waga(li, n - li[p], p + 1) or waga(li, n, p + 1)


def Zadanie_140(T, okreslona_masa):
    return waga(T, okreslona_masa)



```