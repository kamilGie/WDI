# ====================================================================================================>
# Zadanie 42
# Proszę napisać funkcję, która zwraca wartość True gdy dwie liczby są zbudowane z tych
# samych cyfr (na przykład: 123 i 231, 5749 i 4597) i wartość False w przeciwnym przypadku.
# ====================================================================================================>


def policz_wystapienia_cyfry(liczba, cyfra):
    wystapienia = 0
    while liczba > 0:
        liczba, d = divmod(liczba, 10)
        if d == cyfra:
            wystapienia += 1
    return wystapienia


def Zadanie_42(a, b):
    for i in range(10):
        if policz_wystapienia_cyfry(a, i) != policz_wystapienia_cyfry(b, i):
            return False
    return True
