def sposob1():
    a = 1
    b = 1
    while True:
        A = a
        B = b
        while A < 2024:
            A, B = A + B, A
        if A == 2024:
            break

        if a == 0:
            a = b + 1
            b = 0
        else:
            a -= 1
            b += 1

    print(f"suma{a+b}, a={a} b={b} ")


def sposob2():
    suma = 10000
    best = (0, 0)
    for i in range(1, 2023):
        x = i
        y = 2024

        while x > 0 and y > x:
            x, y = y - x, x

        if x + y < suma:
            best = (x, y)
            suma = x + y
    print(suma, best)


sposob1()
sposob2()
