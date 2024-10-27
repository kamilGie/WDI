from math import sqrt


def average(a, b):
    while abs(a-b) > 0.000001:
        a, b = sqrt(a*b), (a+b)/2
    return a


print(average(4, 7))