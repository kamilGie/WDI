![Zadanie 140](../../srt/zbior_zadan/140.png)
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