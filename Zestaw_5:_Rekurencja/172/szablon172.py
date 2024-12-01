# ====================================================================================================>
# Zadanie 172
# Proszęn apisać rekurencyjną funkcję obliczającą n-ty wyraz ciągu Fibonacciego ale tak aby
# wewnątrz funkcji było tylko jedno odwołanie rekurencyjne.
# ====================================================================================================>


def fibonacci(n): ...


if __name__ == "__main__":
    from testy172 import odpal_testy

    fibonacci(int(input("Podaj n: ")))

    # odpal_testy()
