<picture>
  <source srcset="../../srt/zbior_zadan/167.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_167.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_167.png" alt="zadanie 167">
</picture>

```python
def Zadanie_167(slowo):
    samogloski = {"a", "e", "i", "o", "u"}

    # tablica pozycji samoglosek w slowo
    pozycje = []
    for i in range(len(slowo)):
        if slowo[i] in samogloski:
            pozycje.append(i)

    if len(pozycje) < 2: return 0

    # liczba możliwych kombinacji to odległości między samogloskami
    res = 1
    for i in range(1, len(pozycje)):
        res *= pozycje[i] - pozycje[i - 1]

    return res
```
# Opis Rozwiązania

### Przykładowe wywołanie

Dla słowa `bbbabbabb` pozycje samogłosek to 3 i 6. Ich odległość wynosi 3, co oznacza, że mamy 3 kombinacje,
ponieważ możemy zawsze przenieść jedną z liter między lewym a prawym przecięciem, a taka operacja będzie
możliwa dla każdej odległości.
