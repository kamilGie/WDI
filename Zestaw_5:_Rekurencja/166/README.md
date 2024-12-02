![Zadanie 166](../../srt/zbior_zadan/166.png)
```python
def buduj_prawo(T, T_nastepne, prawo, napis):
    """
    Rekurencyjna funkcja, która, sklejając napisy, szuka takiego napisu w
    tablicy, który zaczyna się od ostatnio zakończonego napisu drugiej tablicy.

    Następnie, z tego znalezionego napisu, odcina początek, który stanowiło 'prawo',
    i ustawia go jako nowe 'prawo'.

    Tworzy kopię tablicy bez tego napisu i wykonuje się rekurencyjnie. Funkcja będzie
    działać, dopóki 'prawo' nie stanie się puste lub nie znajdzie napisu zaczynającego się
    od 'prawo'.

    Jeśli 'prawo' jest puste, oznacza to, że albo wykorzystaliśmy wszystkie napisy, albo wybraliśmy niewłaściwy napis.
    """

    if prawo == "":
        return napis if len(T) == 0 else False

    for i, t in enumerate(T):

        if t.startswith(prawo):
            nowa_lista = T[:i] + T[i + 1 :]
            nowe_prawo = t[len(prawo) :]
            res = buduj_prawo(T_nastepne, nowa_lista, nowe_prawo, napis + nowe_prawo)
            if res:
                return res

        elif t in prawo:
            nowa_lista = T[:i] + T[i + 1 :]
            nowe_prawo = prawo[len(t) :]
            res = buduj_prawo(nowa_lista, T_nastepne, nowe_prawo, napis)
            if res:
                return res

    return False


def Zadanie_166(T1, T2):
    """
    Należy najpierw znaleźć taki napis w tablicach, który
    zaczyna się od drugiego napisu, aby znaleźć początek.

    Następnie, na podstawie tego drugiego napisu bez poczatku
    pierwszego napisu, generować elementy 'prawe' w rekurencyjnej funkcji.
    """

    for i, t1 in enumerate(T1):
        for j, t2 in enumerate(T2):
            if t1.startswith(t2) or t2.startswith(t1):
                nowa_T1, nowa_T2 = T1[:i] + T1[i + 1 :], T2[:j] + T2[j + 1 :]

                if t1.startswith(t2):
                    res = buduj_prawo(nowa_T2, nowa_T1, t1[len(str(t2)) :], t1)
                else:
                    res = buduj_prawo(nowa_T1, nowa_T2, t2[len(t1) :], t2)

                if res:
                    return res

    return False

```