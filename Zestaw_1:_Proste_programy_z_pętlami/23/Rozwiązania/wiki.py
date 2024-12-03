# ====================================================================================================>
# Zadanie 23
# Dane są ciągi: An+1 = sqrt(An*Bn) oraz Bn+1 =(An +Bn)/2.0.
# Ciągite są zbieżne dowspólnej granicy nazywanej średnią arytmetyczno-geometryczną.
# Proszę napisać program wyznaczający średnią arytmetyczno-geometryczną dwóch liczb naturalnych.
# ====================================================================================================>


from math import sqrt


def average(a, b):
    while abs(a - b) > 0.000001:
        a, b = sqrt(a * b), (a + b) / 2
    # end while
    return (a + b) / 2


