def func(x):
    return 1/x

def calc_area(k, step = 0.0001):
    area = 0
    x = 1
    while x < k:
        area += step*func(x)
        x += step

    return area

k = int(input())
print(calc_area(k))