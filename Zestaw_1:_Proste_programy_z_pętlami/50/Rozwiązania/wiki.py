# ====================================================================================================>
# Zadanie 50
# Pewnych liczb nie można przedstawić jako sumy elementów spójnych fragmentów ciągu
# Fibonacciego, np. 9,14,15,17,22. Proszę napisać program, który wczytuje liczbę naturalną n, wylicza i
# wypisuje następną taką liczbę większą od n. Można założyć, że 0<n<1000.
# ====================================================================================================>


# Julia Smerdel
def fib_exists(num):
    a1, a2, b1, b2 = 1, 1, 1, 1
    fib_sum = 1

    while num != fib_sum:
        if num > fib_sum:
            fib_sum += a2
            a1, a2 = a2, a1 + a2
        if num < fib_sum:
            fib_sum -= b1
            b1, b2 = b2, b1 + b2
        if num < a2:
            break

    return num == fib_sum


def Zadanie_50(n):
    while fib_exists(n + 1):
        n += 1

    return n + 1
