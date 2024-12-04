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


def wyraz(s1, s2): ...


if __name__ == "__main__":
    from testy149 import odpal_testy

    wyraz(str(input("Podaj s1: ")), str(input("Podaj s2: ")))

    # odpal_testy()
