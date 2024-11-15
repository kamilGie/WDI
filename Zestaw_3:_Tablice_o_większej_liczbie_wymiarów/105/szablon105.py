# ====================================================================================================>
# Zadanie 105
# Dwie liczby naturalne są zgodne jeżeli w zapisie dwójkowym zawierają tę samą liczbę
# jedynek,np.22=10110 i 14=1110 . Dane są tablice T1[N1][N1] T2[N2][N2], gdzie N2 ¿ N1.Proszę napisać
# funkcję, która sprawdza czy istnieje takie położenie tablicy T1 wewnątrz tablicy T2, przy którym liczba
# zgodnych elementów jest większa od 33%. Do funkcji należy przekazać tablicę T1 i T2. Obie oryginalne
# tablice powinny pozostać nie zmieniane.
# ====================================================================================================>
# return bool


def Zadanie_105(T1, T2): ...


if __name__ == "__main__":
    from testy105 import odpal_testy

    Zadanie_105(int(input('Podaj T1: ')), int(input('Podaj T2: ')))

    # odpal_testy()
