<picture>
  <source srcset="../../srt/zbior_zadan/139.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_139.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_139.png" alt="zadanie 139">
</picture>

```python
def Zadanie_139(N):
    """
    Mnożymy przez 2, 3 i 5, a w ten sposób otrzymujemy wszystkie liczby dwu-trzy-piątkowe.

    Dla optymalizacji i usunięcia powtórzeń:
    Jeśli liczba powstała z pomnożenia przez 2, to możemy pomnożyć ją przez 2, 3 lub 5.
    Jeśli liczba powstała z pomnożenia przez 3, aby uniknąć powtórzeń, mnożymy ją tylko przez 3 i 5.
    Jeśli liczba powstała z pomnożenia przez 5, aby uniknąć powtórzeń, mnożymy ją tylko przez 5.
    """

    def mnozenie(liczba, ostatnie_mnozenie):
        if liczba > N:
            return

        print(liczba)

        mnozenie(liczba * 5, 5)
        if ostatnie_mnozenie <= 3:
            mnozenie(liczba * 3, 3)
        if ostatnie_mnozenie <= 2:
            mnozenie(liczba * 2, 2)

    mnozenie(1, 1)

```