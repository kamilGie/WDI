<picture>
  <source srcset="../../srt/zbior_zadan/07.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_07.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_07.png" alt="zadanie 07">
</picture>

```python
# podjebane z bitu xd nawet nie patrzylem czy testy sie zgadzaja


def newton_cuberoot(n):
    epsilon = 1e-10
    x = n / 2

    while True:
        next_x = x - (x**3 - n) / (3 * x**2)

        if abs(next_x - x) < epsilon:
            break

        x = next_x

    return x

```