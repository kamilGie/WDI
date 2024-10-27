from math import sqrt


n = int(input())

maxi = sqrt(n)
for i in range(1, int(sqrt(n))):
    an = i**2 + i + 1
    if n%an == 0:
        print("tak")
        break
else:
    print("nie")