from math import sqrt


num = int(input())

maxi = sqrt(num)
a1, a2 = 1, 1

while a1 < maxi:
    if num % a1 == 0:
        b1, b2 = a1, a2
        while a1*b1 < num:
            b1, b2 = b2, b1+b2
        if a1*b1 == num:
            print("da się")
            break
    a1, a2 = a2, a1+a2
else:
    print("nie da się")


