<picture>
  <source srcset="../../srt/zbior_zadan/165.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_165.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_165.png" alt="zadanie 165">
</picture>

```python
def Zadanie_165(T, k):
    def rek(T, k, i, a, b, suma):

        if suma == 0 and a != 0 and b != 0:
            if a + b == k:
                return True

        if i == len(T):
            return False

        return (
            rek(T, k, i + 1, a + 1, b, suma + T[i])
            or rek(T, k, i + 1, a, b + 1, suma - T[i])
            or rek(T, k, i + 1, a, b, suma)
        )

    # end def rek

    return rek(T, k, 0, 0, 0, 0)



```