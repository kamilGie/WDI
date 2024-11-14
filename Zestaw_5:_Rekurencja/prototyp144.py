# ====================================================================================================>
# Zadanie 144
# Dana jest tablica T[N]. Proszę napisać program zliczający liczbę “enek” o określonym
# iloczynie.
# ====================================================================================================>

# cos nie dzialaja
# z wiki ale zmienilem zmienna globalna wiec moze cos tutaj


def zliczanie(T, s, n, p, licznik=0):
    if n == 1:
        for i in range(p, len(T)):
            if T[i] == s:
                licznik += 1
        return licznik

    else:
        for i in range(p, len(T)):
            if s % T[i] == 0:
                return zliczanie(T, s // T[i], n - 1, i + 1, licznik)


def Zadanie_144(T, okreslony_iloczyn, liczba_enek):
    return zliczanie(T, okreslony_iloczyn, liczba_enek, 0)


if __name__ == "__main__":
    from Develop import stworz_zadanie

    stworz_zadanie([Zadanie_144])
