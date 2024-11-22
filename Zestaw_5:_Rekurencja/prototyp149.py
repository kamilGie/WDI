# ====================================================================================================>
# Zadanie 149
# Wyrazy budowane są z liter a..z. Dwa wyrazy ”ważą” tyle samo jeżeli: mają tę samą
# liczbę samogłosek oraz sumy kodów ascii liter z których są zbudowane są identyczne, na przykład ′′ula′′ →
# 117,108,97oraz′′exe′′ →101,120,101.Proszęnapisaćfunkcjęwyraz(s1,s2),którasprawdzaczyjestmożliwe
# zbudowaniewyrazuzpodzbioruliterzawartychws2ważącegotylecowyrazs1.Dodatkowofunkcjapowinna
# wypisać znaleziony wyraz.
# ====================================================================================================>


def liczba_samoglosek(s):
    counter = 0
    n = len(s)
    for i in range(n):
        if czy_samogloska(s[i]):
            counter += 1
    # end for
    return counter


def czy_samogloska(z):
    elements = {"a", "e", "i", "o", "u", "y"}
    if z in elements:
        return True
    # end if
    return False


def waga_wyrazu(s):
    suma = 0
    n = len(s)
    for i in range(n):
        suma += ord(s[i])
    # end for
    return suma


def Zadanie_149(s,T):  # s - wyraz
    def rek(s, x, T):
        if waga_wyrazu(x) > waga_wyrazu(s):
            return False

        if waga_wyrazu(x) == waga_wyrazu(s):
            if liczba_samoglosek(x) == liczba_samoglosek(s):
                print(x)
                return True

        for z in T:
            if rek(s, x + z, T):
                return True

        return False

    Zadanie_149(s, ["u", "l", "a"])


if __name__ == "__main__":
    from Develop import stworz_zadanie

    Zadanie_149()
    # stworz_zadanie([Zadanie_149])
