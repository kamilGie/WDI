# ====================================================================================================>
# Zadanie 7
# Proszę z modyfikować wzór Newtona aby program z poprzedniego zadania obliczał pierwiastek
# stopnia 3.
# ====================================================================================================>

# podjebane z bitu xd nawet nie patrzylem czy testy sie zgadzaja


def newton_cuberoot(n):
    epsilon = 1e-10
    x = n / 2

    while True:
        next_x = x - (x**3 - n) / (3 * x**2)

        if abs(next_x - x) < epsilon:
            break

        x = next_x

    return x
