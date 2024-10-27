from math import sqrt


def czy_pierwsza(n):
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False

    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0: return False

    return True




