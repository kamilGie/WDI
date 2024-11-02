# ====================================================================================================>
# Zadanie 23
# Dane są ciągi: An+1 = sqrt(An*Bn) oraz Bn+1 =(An +Bn)/2.0.
# Ciągite są zbieżne dowspólnej granicy nazywanej średnią arytmetyczno-geometryczną.
# Proszę napisać program wyznaczający średnią arytmetyczno-geometryczną dwóch liczb naturalnych.
# ====================================================================================================>


def average(a, b): ...


if __name__ == "__main__":
    from testy23 import odpal_testy

    average(int(input('Podaj a: ')), int(input('Podaj b: ')))

    # odpal_testy()
