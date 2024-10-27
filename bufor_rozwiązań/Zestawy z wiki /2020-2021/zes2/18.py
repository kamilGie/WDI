# Zadanie 18. 
# Mamy dane dwa ciągi A,B o następujących zależnościach:
# A: a 0 = 0, a 1 = 1, a n = a n−1 − b n−1 ∗ a n−2
# B: b 0 = 2, b n = b n−1 + 2 ∗ a n−1
# Proszę napisać program, który czyta liczby typu int ze standardowego wejścia i tak długo jak liczby te są
# kolejnymi wyrazami ciągu A n (tj. a 0 , a 1 , a 2 , ...) wypisuje na standardowe wyjście wyrazy drugiego ciągu B n
# (tj. b 0 , b 1 , b 2 , ...).


a0, a1 = 0, 1
b0 = 2
b1 = b0 + 2*a0

if int(input()) == a0:
    print("b", b0)
else:
    exit()

while int(input()) == a1:
    print("b", b1)

    a0, a1 = a1, a1 - b1*a0
    b0, b1 = b1, b1 + 2*a0