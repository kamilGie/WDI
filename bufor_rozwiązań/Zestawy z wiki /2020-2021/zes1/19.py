def calc(prec = 50):
    fac = 1
    c = 0
    for i in range(1, prec):
        c += 1/fac
        fac *= i
    return c

print(calc())