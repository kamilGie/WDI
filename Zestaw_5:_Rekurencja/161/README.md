<picture>
  <source srcset="../../srt/zbior_zadan/161.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_161.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_161.png" alt="zadanie 161">
</picture>

```python
def policz_jedynki_binarnie(liczba):
    licznik = 0
    while liczba > 0:
        licznik += liczba % 2
        liczba //= 2
    return licznik


def Zadanie_161(T):
    # Przechowuje liczbe jedynek w zapisie binarnym każdej liczby z T.
    tablica_jedynek = [policz_jedynki_binarnie(x) for x in T]

    suma_jedynek = sum(tablica_jedynek)
    if suma_jedynek % 3 != 0:
        return False

    cel = suma_jedynek // 3

    def czy_mozna_podzielic(A, B, C, indeks):
        if indeks == len(T):
            return True

        liczba = tablica_jedynek[indeks]

        if A + liczba <= cel and czy_mozna_podzielic(A + liczba, B, C, indeks + 1):
            return True
        if B + liczba <= cel and czy_mozna_podzielic(A, B + liczba, C, indeks + 1):
            return True
        if C + liczba <= cel and czy_mozna_podzielic(A, B, C + liczba, indeks + 1):
            return True

        return False

    return czy_mozna_podzielic(0, 0, 0, 0)
```

# Opis Rozwiązania:
## `Zadanie_161`

### `tablica_jedynek`
Przechowuje liczbe jedynek w zapisie binarnym każdej z liczby z T. np:
- `T=[3, 5, 7, 10, 15]`
- `tablica_jedynek=[2,2,3,2,4]`
        

Jeśli podzbiór ma istnieć, suma całej `tablicy_jedynek` musi być podzielna przez 3, a wynik
dzielenia tej sumy przez 3 będzie docelową sumą dla każdego podzbioru.

### `czy_mozna_podzielic`
Rekurencyjnie tworzę 3 sumy: `A`, `B`, `C`. Dodając do każdej z nich wartości z `tablicy_jedynek` sprawdzam,
czy jakaś kombinacja pozwoli rozdzielić liczby tak, aby suma w żadnym z podzbiorów nie przekroczyła docelowej wartości.
Jeśli uda się rozdzielić wszystkie elementy z tablicy jedynek i nie przekroczyć docelowej sumy, to podział jest możliwy.

