# ====================================================================================================>
# Zadanie 149
# Wyrazy budowane są z liter a..z. Dwa wyrazy ”ważą” tyle samo jeżeli: mają tę samą
# liczbę samogłosek oraz sumy kodów ascii liter z których są zbudowane są identyczne, na przykład ′′ula′′ →
# 117,108,97oraz′′exe′′ →101,120,101.Proszę napisać funkcję wyraz(s1,s2), która sprawdza czy jest możliwe
# zbudowanie wyrazu z podzbioru liter zawartych w s2 ważącego tyle co wyraz s1. Dodatkowo funkcja powinna
# wypisać znaleziony wyraz.
# ====================================================================================================>
# jak sie da wypisz wyraz zwroc True
# jak sie nie da zwroc False


def suma_asci(napis):
    return sum(ord(ch) for ch in napis)


def kombinacje(litery, k):
    """
    Rekurencyjna funkcja zwracająca wszystkie kombinacje liter (napisy) o długości k.

    Funkcja bierze pierwszą literę ze zbioru, a następnie wywołuje się
    rekurencyjnie z pozostałą częścią zbioru (bez tej litery) oraz z k-1.

    Następnie funkcja wywołuje się również na zbiorze bez pierwszej litery,
    ale z zachowaniem tej samej długości k. Dzięki temu otrzymujemy wszystkie
    możliwe kombinacje, które są zwracane w postaci listy napisów.

    Oryginalnie ta funkcja powinna być generatorem,ale może to być zbyt zaawansowane
    narzędzie więc zostało zmienione aby zwracało listę wyników.
    """
    if k == 0:
        return [""]
    if len(litery) < k:
        return []

    z_pierwsza_litera = [litery[0] + comb for comb in kombinacje(litery[1:], k - 1)]
    bez_pierwszej_litery = kombinacje(litery[1:], k)

    return z_pierwsza_litera + bez_pierwszej_litery


def wyraz(s1, s2):
    """
    Zbiór `s2` dzielę na dwa podzbiory: spółgłoski i samogłoski. Następnie z podzbioru samogłosek generuję
    napisy, które mają długość równą liczbie samogłosek w `s1`. Dla tych napisów obliczam wymaganą sumę,
    która jest potrzebna, aby osiągnąć sumę ASCII `s1`. Następnie ze zbioru spółgłosek generuję napisy,
    i sprawdzam czy w sumie ASCII dają wymaganą wartość.
    """

    samogloski = {"a", "e", "i", "o", "u", "y"}
    samogloski_s2 = [ch for ch in s2 if ch in samogloski]
    spolgloski_s2 = [ch for ch in s2 if ch not in samogloski]
    liczba_samoglosek_s1 = sum(1 for ch in s1 if ch in samogloski)

    for samogloskowy_napis in kombinacje(samogloski_s2, liczba_samoglosek_s1):
        wymagana_suma = suma_asci(s1) - suma_asci(samogloskowy_napis)

        for k in range(len(spolgloski_s2) + 1):
            for spolgloskowy_napis in kombinacje(spolgloski_s2, k):
                if suma_asci(spolgloskowy_napis) == wymagana_suma:
                    print(samogloskowy_napis + spolgloskowy_napis)
                    return True

    return False


if __name__ == "__main__":
    from testy149 import odpal_testy

    wyraz(str(input("Podaj s1: ")), str(input("Podaj s2: ")))

    odpal_testy()
