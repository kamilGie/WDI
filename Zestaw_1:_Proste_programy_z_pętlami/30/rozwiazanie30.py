# ====================================================================================================>
# Zadanie 30
# Proszę napisać program, który oblicza pole figury pod wykresem funkcji y =1/x w przedziale
# od 1 do k, metodą prostokątów.
# ====================================================================================================>
# nie jestem tego pewny


def pole(k):
    eps = 0.0001
    x = 1
    suma = 0

    while x < k:
        suma += (1 / x) * eps
        x += eps

    return suma


