# ====================================================================================================>
# Zadanie 2B, 2024-01-04
# Na liczbach naturalnych możemy wykonywać następujące operacje:
# 1. 𝐴(𝑛) zamienia liczbę 𝑛 na sumę jej podzielników właściwych (mniejszych od samej liczby), np.
# 𝐴(1) = 1, 𝐴(6) = 6, 𝐴(12) = 16, 𝐴(17) = 1.
# 2. 𝐵(𝑛) zamienia liczbę 𝑛 na najmniejszy, większy od tej liczby wyraz ciągu Fibonacciego, np.
# 𝐵(1) = 2, 𝐵(4) = 5, 𝐵(8) = 13.
# 3. 𝐶(𝑛) zwiększa liczbę 𝑛 o liczbę będącą rewersem liczby 𝑛, np. 𝐶(1) = 2, 𝐶(10) = 11, 𝐶(13) = 44
# Proszę napisać funkcję cycle(x,n), która sprawdza czy startując od liczby 𝑥 możemy do niej powrócić
# wykonując sekwencję operacji spośród A,B,C o długości większej od 1 i nie większej od n. Jeżeli jest to
# możliwe, funkcja powinna zwrócić długość znalezionej sekwencji operacji, w przeciwnym wypadku
# należy zwrócić wartość 0.
# Na przykład wywołanie:
# cycle(29,6) powinno zwrócić 4 (cykl 29, B, 55, B, 89, C, 187, A, 29), [przykład jest błędny, 𝐵(29) = 34]
# cycle(31,6) powinno zwrócić 0.
# ====================================================================================================>
# Autor rozwiązania Kamil Gieras
# Uwaga: Przykład podany w zadaniu jest błędny: B(29) --> 34, nie 55

from math import isqrt


def a(n):
    res = 1
    if n == 1:
        return res
        
    for i in range(2, isqrt(n)):
        if n % i == 0:
            res += i
            res += n // i

    if isqrt(n) ** 2 == n:
        res += isqrt(n)
    return res


def b(n):
    a, b = 1, 1
    while a <= n:
        a, b = a + b, a
    return a


def c(n):
    # return n + int(str(n)[::-1])
    reverse = 0
    kopia = n
    while kopia > 0:
        kopia, d = divmod(kopia, 10)
        reverse = reverse * 10 + d
    return n + reverse


def cycle(x, n):
    def rek(l, i):
        if l == x:
            return n - i  # powrocila
        if i == 0:
            return 0
        return max(rek(a(l), i - 1), rek(b(l), i - 1), rek(c(l), i - 1))

    # zwracam max dlugosci łańcucha jesli nie bedzie zadnego to max zwróci 0
    return max(rek(a(x), n - 1), rek(b(x), n - 1), rek(c(x), n - 1))
