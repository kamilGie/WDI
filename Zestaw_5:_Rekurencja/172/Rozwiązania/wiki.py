# ====================================================================================================>
# Zadanie 172
# Proszęn apisać rekurencyjną funkcję obliczającą n-ty wyraz ciągu Fibonacciego ale tak aby
# wewnątrz funkcji było tylko jedno odwołanie rekurencyjne.
# ====================================================================================================>


def fibonacci(n, a=0, b=1):
    """
    Rekurencyjna wersja pętli for, która wykonuje się, dopóki n jest większe niż 0,
    z możliwością ustawienia dwóch początkowych elementów ciągu.
    Domyślne wartości a=0 i b=1 odpowiadają pierwszym dwóm wyrazom ciągu Fibonacciego.
    """
    return fibonacci(n - 1, b, a + b) if n > 0 else a
