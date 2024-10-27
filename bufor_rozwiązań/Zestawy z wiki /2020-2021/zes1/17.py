def golden_ratio(prec = 50):
    a, b = 1, 1
    old_ratio, ratio = 1, 0
    # for _ in range(prec):
    while abs(old_ratio - ratio) > 0.00000000001:
        a, b = b, a+b
        old_ratio, ratio = ratio, b/a
    return b/a


print(golden_ratio())
