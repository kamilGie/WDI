def pole(k):
    eps = 0.0001
    x = 1
    area = 0

    while x < k:
        area = eps/x
        x += eps

    return area
