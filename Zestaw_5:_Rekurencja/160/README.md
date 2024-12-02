![Zadanie 160](../../srt/zbior_zadan/160.png)
```python
def pole(proste) -> int:
    return (proste[1] - proste[0]) ** 2


def nachodza(k1, k2) -> bool:
    """ Nachodzenie zachodzi, jeśli kwadrat nie leży całkowicie po lewej, prawej, poniżej lub powyżej drugiego. """
    lewo, prawo = k1[1] <= k2[0], k1[0] >= k2[1]
    dol, gora = k1[3] <= k2[2], k1[2] >= k2[3]

    return not (lewo or prawo or dol or gora)


def Zadanie_160(T):
    """
    Sortujemy kwadraty według pola malejąco, aby zoptymalizować wyszukiwanie.
    Następnie rekurencyjnie szukamy kombinacji kwadratów, tworząc listę odpowiadających kwadratów.
    Jeśli kwadrat nie nachodzi na żaden z kwadratów w tej liście, sprawdzamy, czy funkcja, dodając go do
    listy oraz zmniejszając szukane pole o pole tego kwadratu, zwróci wartość True.
    Zwracamy True, jeśli na liście znajduje się 13 kwadratów, a `szukane_pole` wynosi 0.
    Zwracamy False, jeśli doszliśmy do końca listy kwadratów, lista kwadratów jest za duża lub suma pól przekroczyła 0.
    """
    T.sort(key=pole, reverse=True)
    wymagana_liczba_kwadratow = 13
    wymagane_pole_kwadratow = 2012

    def rek(idx=0, szukane_pole=wymagane_pole_kwadratow, kwadraty=[]):
        if len(kwadraty) == wymagana_liczba_kwadratow and szukane_pole == 0:
            return True
        if idx == len(T) or len(kwadraty) > wymagana_liczba_kwadratow or szukane_pole < 0:
            return False

        if not any(nachodza(T[idx], kwadrat) for kwadrat in kwadraty):
            if rek(idx + 1, szukane_pole - pole(T[idx]), kwadraty + [T[idx]]):
                return True

        return rek(idx + 1, szukane_pole, kwadraty)

    return rek()

```