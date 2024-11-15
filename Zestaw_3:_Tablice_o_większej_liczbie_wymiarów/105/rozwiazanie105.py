# ====================================================================================================>
# Zadanie 105
# Dwie liczby naturalne są zgodne jeżeli w zapisie dwójkowym zawierają tę samą liczbę
# jedynek,np.22=10110 i 14=1110 . Dane są tablice T1[N1][N1] T2[N2][N2], gdzie N2 ¿ N1.Proszę napisać
# funkcję, która sprawdza czy istnieje takie położenie tablicy T1 wewnątrz tablicy T2, przy którym liczba
# zgodnych elementów jest większa od 33%. Do funkcji należy przekazać tablicę T1 i T2. Obie oryginalne
# tablice powinny pozostać nie zmieniane.
# ====================================================================================================>
# return bool


def compare(a, b):
    cnt = 0
    while a != 0:
        cnt += a % 2
        a = a // 2

    while b != 0:
        cnt -= b % 2
        b = b // 2

    return cnt == 0


def Zadanie_105(T1, T2):
    n, m = len(T1), len(T2)  # n < m
    cnt = 0

    for y in range(m - n + 1):
        for x in range(m - n + 1):
            cnt = 0
            for a in range(n):
                for b in range(n):
                    if compare(T1[a][b], T2[y + a][x + b]):
                        cnt += 1

            if cnt / (n * n) > 0.33:
                print(y, x)
                return True
    return False


