# ====================================================================================================>
# Zadanie 11
# Proszę napisać program wypisujący podzielniki liczby.
# ====================================================================================================>
# wypisujacy wiec testy sprawdzaja print


def divisors(n):
    if n == 0:
        print("Każda")
        return

    i = 1
    while i * i < n:
        if n % i == 0:
            print(n // i, i)
        i += 1

    if i * i == n:
        print(i)


if __name__ == "__main__":
    from testy11 import odpal_testy

    divisors(int(input("Podaj n: ")))

    odpal_testy()
