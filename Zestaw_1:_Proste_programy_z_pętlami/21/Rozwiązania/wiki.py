# ====================================================================================================>
# Zadanie 21
# Proszę napisać program wyznaczający wartość do której zmierza iloraz dwóch kolejnych
# wyrazów ciągu Fibonacciego. Wyznaczyć ten ilorazy dla różnych wartości dwóch początkowych wyrazów
# ciągu.
# ====================================================================================================>


def golden_ratio(a, b):
    while abs((b / a) - (a + b) / b) > 0.00001:
        a, b = b, a + b

    return b / a


