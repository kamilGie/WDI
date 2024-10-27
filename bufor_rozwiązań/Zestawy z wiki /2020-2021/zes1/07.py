def isFibProduct(num):
    a, b = 1, 1
    while a*b < num:
        a, b = b, a+b
    if a*b == num:
        return True
    else:
        return False


print(isFibProduct(int(input())))