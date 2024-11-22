# ====================================================================================================>
# Zadanie 145
# Proszę zmodyfikować poprzedni program aby wypisywał znalezione n-ki.
# ====================================================================================================>


def rek(t, il, left, i=0, n=None, already_choosen=False, history=None):
    history = history or []
    n = n or len(t)

    if left == 0 or i == n:
        if left == 0 and il == 1 and already_choosen:
            print(history)
        return

    rek(t, il, left, i + 1, n, already_choosen, [*history])

    if il % t[i] == 0:
        rek(t, il // t[i], left - 1, i + 1, n, True, [*history, t[i]])

    return


def Zadanie_145(tablica, okreslony_iloczyn, liczba_elementow):
    rek(tablica, okreslony_iloczyn, liczba_elementow)


