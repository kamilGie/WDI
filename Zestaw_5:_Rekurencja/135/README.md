<picture>
  <source srcset="../../srt/zbior_zadan/135.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_135.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_135.png" alt="zadanie 135">
</picture>

```python
def f(T, w, k):

    if w == 7:
        return T[w][k]

    if k > 0:
        left = f(T, w + 1, k - 1)
    else:
        left = float("inf")

    if k < 7:
        right = f(T, w + 1, k + 1)
    else:
        right = float("inf")

    middle = f(T, w + 1, k)

    return min(left, middle, right) + T[w][k]


def Zadanie_135(t, k):
    return f(t, 0, k)



```