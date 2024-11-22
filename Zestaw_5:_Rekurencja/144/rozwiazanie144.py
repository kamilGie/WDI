# ====================================================================================================>
# Zadanie 144
# Dana jest tablica T[N]. Proszę napisać program zliczający liczbę “enek” o określonym
# iloczynie.
# ====================================================================================================>
# return liczba enek


def rek(t, il, left, i=0, n=None, already_choosen=False, history=None, counter=0):
    history = history or []
    n = n or len(t)

    if left == 0 or i == n:
        if left == 0 and il == 1 and already_choosen:
            return counter + 1
        return counter

    counter = rek(t, il, left, i + 1, n, already_choosen, [*history], counter)

    if il % t[i] == 0:
        counter = rek(
            t, il // t[i], left - 1, i + 1, n, True, [*history, t[i]], counter
        )

    return counter


def Zadanie_144(tablica, okreslony_iloczyn, liczba_elementow):
    return rek(tablica, okreslony_iloczyn, liczba_elementow)


