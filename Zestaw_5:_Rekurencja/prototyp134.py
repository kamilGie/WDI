# ====================================================================================================>
# Zadanie 134
# ”Waga” liczby jest określona jako ilość różnych czynników pierwszych liczby. Na przykład
# waga(1)=0, waga(2)=1, waga(6)=2, waga(30)=3, waga(64)=1. Dana jest tablica T[N] zawierająca liczby
# naturalne. Proszę napisać funkcję, która sprawdza czy można elementy tablicy podzielić na 3 podzbiory o
# równych wagach. Do funkcji należy przekazać wyłącznie tablicę, funkcja powinna zwrócić wartość typu Bool.
# ====================================================================================================>


from math import sqrt

# cos jest zlego w tej funkcji


def diff_div(n):
    k = n
    i = 2
    pom = 0
    cnt = 0
    while i <= sqrt(k) + 1:
        while n % i == 0:
            pom += 1
            n = n // i
        if pom > 0:
            cnt += 1
        pom = 0
        i += 1
    return cnt


def wagi(t, a=0, b=0, c=0, n=0):
    if n == len(t) - 1:
        return a == b == c
    else:
        return (
            wagi(t, a + diff_div(t[n]), b, c, n + 1)
            or wagi(t, a, b + diff_div(t[n]), c, n + 1)
            or wagi(t, a, b, c + diff_div(t[n]), n + 1)
        )


if __name__ == "__main__":
    from Develop import stworz_zadanie

    stworz_zadanie([wagi])
