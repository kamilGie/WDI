def newton_raphson(num, ep = 0.000001):
    a, b = 1, num
    while abs(a-b) > ep:
        a = (a+b)/2
        b = num/a
    return a


print(newton_raphson(9))