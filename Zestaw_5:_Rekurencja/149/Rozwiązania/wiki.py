# ====================================================================================================>
# Zadanie 149
# Wyrazy budowane są z liter a..z. Dwa wyrazy ”ważą” tyle samo jeżeli: mają tę samą
# liczbę samogłosek oraz sumy kodów ascii liter z których są zbudowane są identyczne, na przykład ′′ula′′ →
# 117,108,97oraz′′exe′′ →101,120,101.Proszę napisać funkcję wyraz(s1,s2), która sprawdza czy jest możliwe
# zbudowanie wyrazu z podzbioru liter zawartych w s2 ważącego tyle co wyraz s1. Dodatkowo funkcja powinna
# wypisać znaleziony wyraz.
# ====================================================================================================>
# jak sie da wypisz wyrazi zwroc True
# jak sie nie da zwroc False


def suma_asci(napis):
    return sum(ord(ch) for ch in napis)


def kombinacje(litery, k):
    if k == 0:
        yield ""
        return
    if len(litery) < k:
        return

    # Kombinacje z pierwszą literą
    for comb in kombinacje(litery[1:], k - 1):
        yield litery[0] + comb

    # Kombinacje bez pierwszej litery
    yield from kombinacje(litery[1:], k)


def wyraz(s1, s2):
    samogloski = {"a", "e", "i", "o", "u", "y"}

    # Zbiór `s2` dzielę na dwa podzbiory: spółgłoski i samogłoski.
    samogloski_s2 = []
    spolgloski_s2 = []
    for ch in s2:
        if ch in samogloski:
            samogloski_s2.append(ch)
        else:
            spolgloski_s2.append(ch)

    # licze samogloski w s1
    liczba_samoglosek_s1 = 0
    for ch in s1:
        if ch in samogloski:
            liczba_samoglosek_s1 += 1

    # Z podzbioru samogłosek generuję napisy, które mają długość równą liczbie samogłosek w `s1`.
    for samogloskowy_napis in kombinacje(samogloski_s2, liczba_samoglosek_s1):
        wymagana_suma = suma_asci(s1) - suma_asci(samogloskowy_napis)

        # Następnie ze zbioru spółgłosek generuję napisy, i sprawdzam czy w sumie ASCII dają wymaganą wartość.
        for k in range(len(spolgloski_s2) + 1):
            for spolgloskowy_napis in kombinacje(spolgloski_s2, k):
                if suma_asci(spolgloskowy_napis) == wymagana_suma:
                    print(samogloskowy_napis + spolgloskowy_napis)
                    return True

    return False
