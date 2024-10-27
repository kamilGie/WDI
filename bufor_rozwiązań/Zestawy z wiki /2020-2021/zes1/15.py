# wyrazy tego nieskończonego iloczynu można przedstawić jako ciąg rekurencyjny
# a(1) = sqrt(0.5)
# a(n) = sqrt(0.5 + 0.5*a(n-1))


from math import sqrt


def calc_pi(prec = 10):
    pi = 2
    a = sqrt(0.5)
    for _ in range(prec):
        pi /= a
        a = sqrt(0.5 + 0.5*a)
    return pi


print(calc_pi())