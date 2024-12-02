<picture>
  <source srcset="../../srt/zbior_zadan/138.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_138.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_138.png" alt="zadanie 138">
</picture>

```python
import math


def Zadanie_138(t):

    def rek(t, i, s_el=0, s_it=0, best=math.inf, l=0, s_best=0):
        if i >= len(t):
            return s_el == s_it and s_el > 0, s_el, l

        s_best = 0
        poss = False

        ans, s, leng = rek(t, i + 1, s_el, s_it, best, l)
        if ans and leng < best:
            best = leng
            s_best = s
            poss = True

        ans, s, leng = rek(t, i + 1, s_el + t[i], s_it + i, best, l + 1)
        if ans and leng < best:
            best = leng
            s_best = s
            poss = True

        return poss, s_best, best

    _, wynik, _ = rek(t, 0)

    return wynik

```