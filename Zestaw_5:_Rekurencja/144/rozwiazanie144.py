# ====================================================================================================>
# Zadanie 144
# Dana jest tablica T[N]. Proszę napisać program zliczający liczbę “enek” o określonym
# iloczynie.
# ====================================================================================================>

# z wiki ale zmienilem zmienna globalna wiec moze cos tutaj

licznik = 0


def zliczanie(T, s, n, p):
    global licznik
    if n == 1:
        for i in range(p, len(T)):
            if T[i] == s:
                licznik += 1

    else:
        for i in range(p, len(T)):
            if s % T[i] == 0:
                zliczanie(T, s // T[i], n - 1, i + 1)


def Zadanie_144(T, okreslony_iloczyn, liczba_enek):
    return zliczanie(T, okreslony_iloczyn, liczba_enek, 0)


