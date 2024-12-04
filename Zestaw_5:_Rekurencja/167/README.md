<picture>
  <source srcset="../../srt/zbior_zadan/167.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_167.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_167.png" alt="zadanie 167">
</picture>

```python
def Zadanie_167(slowo):
    """
    Tworzę tablicę pozycji samogłosek w napisie.
    Dla dwóch kolejnych pozycji mnożę ich odległość przez odległości następnych par.
    """

    samogloski = {"a", "e", "i", "o", "u"}
    pozycje = [i for i, char in enumerate(slowo) if char in samogloski]
    if len(pozycje) < 2: return 0

    res = 1
    for i in range(1, len(pozycje)):
        res *= pozycje[i] - pozycje[i - 1]

    return res

```