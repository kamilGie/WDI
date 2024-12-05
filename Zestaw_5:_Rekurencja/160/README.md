<picture>
  <source srcset="../../srt/zbior_zadan/160.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_160.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_160.png" alt="zadanie 160">
</picture>

```python
def pole(proste) -> int:
    return (proste[1] - proste[0]) ** 2


def nachodza(k1, k2) -> bool:
    """Nachodzenie zachodzi, jeśli kwadrat nie leży całkowicie po lewej, prawej, poniżej lub powyżej drugiego."""
    lewo = k1[1] <= k2[0]
    prawo = k1[0] >= k2[1]
    dol = k1[3] <= k2[2]
    gora = k1[2] >= k2[3]

    return not (lewo or prawo or dol or gora)


def Zadanie_160(T):
    wymagana_liczba_kwadratow = 13
    wymagane_pole_kwadratow = 2012

    def rek(idx=0, szukane_pole=wymagane_pole_kwadratow, kwadraty=[]):

        # Zwracamy True, jeśli na liście znajduje się 13 kwadratów, a `szukane_pole` wynosi 0.
        if len(kwadraty) == wymagana_liczba_kwadratow and szukane_pole == 0:
            return True

        # Zwracamy False, jeśli doszliśmy do końca listy kwadratów, lista kwadratów jest za duża lub suma pól przekroczyła 0.
        if ( idx == len(T) or len(kwadraty) > wymagana_liczba_kwadratow or szukane_pole < 0):
            return False

        # Jeśli kwadrat nie nachodzi na żaden z kwadratów w tej liście, 
        if not any(nachodza(T[idx], kwadrat) for kwadrat in kwadraty):
            # sprawdzamy, czy funkcja, dodając go do listy oraz zmniejszając szukane pole o pole tego kwadratu zwroci true
            if rek(idx + 1, szukane_pole - pole(T[idx]), kwadraty + [T[idx]]):
                return True

        return rek(idx + 1, szukane_pole, kwadraty)

    return rek()
```
# Opis Rozwiązania
## `nachodza`
Nachodzenie zachodzi, jeśli kwadrat nie leży całkowicie po lewej, prawej, poniżej lub powyżej drugiego.

https://github.com/user-attachments/assets/a1187c95-8b86-4e0a-9362-3ba7cd2aa890

można potestowac program dostępny w rozwiązaniach 



