# ====================================================================================================>
# Zadanie 63
# Proszę napisać program obliczający i wypisujący stałą e z rozwinięcia w szereg e = 1/0!+
# 1/1!+1/2!+1/3!+... z dokładnością N cyfr dziesiętnych (N jest rzędu 1000).
# ====================================================================================================>

# wziete z wiki ale nie poprawnie liczy


def long_div(a, b, t):
    t[0] = a // b
    a = a % b
    for i in range(1, len(t)):
        a = a * 10
        t[i] = a // b
        a = a % b
        if a == 0:
            return t

    return t


def Zadanie_63(n):
    n = n + 2
    digits = [1] + [0] * (n)
    tab = [0] * (n + 1)
    fact = 1
    k = 1

    while fact <= 10**n + 1:
        fact *= k
        k += 1
        long_div(1, fact, tab)
        for i in range(n + 1):
            digits[i] += tab[i]

    for i in range(len(digits) - 1, 0, -1):
        digits[i - 1] += digits[i] // 10
        digits[i] %= 10

    print(digits[0], end=".")
    for cyfra in digits[1:-2]:
        print(cyfra, end="")


if __name__ == "__main__":
    from Develop import stworz_zadanie

    stworz_zadanie([Zadanie_63])
