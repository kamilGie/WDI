<picture>
  <source srcset="../../srt/zbior_zadan/139.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_139.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_139.png" alt="zadanie 139">
</picture>

```python
def Zadanie_139(N):
    def mnozenie(liczba, ostatnie_mnozenie):
        """ Mnożymy  przez 2, 3 i 5, a w ten sposób otrzymujemy wszystkie liczby dwu-trzy-piątkowe. """
        if liczba > N:
            return

        print(liczba)

        # Jeśli liczba powstała z pomnożenia przez 5, aby uniknąć powtórzeń, mnożymy ją tylko przez 5.
        mnozenie(liczba * 5, 5)

        # Jeśli liczba powstała z pomnożenia przez 3, aby uniknąć powtórzeń, mnożymy ją tylko przez 3 i 5.
        if ostatnie_mnozenie <= 3:
            mnozenie(liczba * 3, 3)

        # Jeśli liczba powstała z pomnożenia przez 2, to możemy pomnożyć ją przez 2, 3 lub 5.
        if ostatnie_mnozenie <= 2:
            mnozenie(liczba * 2, 2)

    mnozenie(1, 1)
```
# Opis Rozwiązania:
## `Zadanie_139`

![WDI RST](https://github.com/user-attachments/assets/3f2bb7c2-f5ac-4926-b2f7-432ce72d7d36)
