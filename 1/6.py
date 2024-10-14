# Proszę napisać program wyznaczający pierwiastek kwadratowy ze wzoru Newtona.

s = float(input())

a1 = 1
a2 = (s / a1 + a1) / 2
epsilon = 1e-5

while abs(a2 - a1) > epsilon:
    a1 = a2
    a2 = (s / a1 + a1) / 2

print(a2)
