def prime(n):
    if n < 2 :
        return False
    for i in range(2, int(n**(0.5))+1):
        if n%i == 0 :
            return False
    return True


def rek(n, result = 0, pos = 0,b = False):
    if n==0:
        if result > 9 and b and prime(result):
            print(result)
        return
    rek(n // 10, result, pos, True)
    rek(n // 10, result + ((n%10) * 10 ** pos), pos + 1, b)


print(rek(313))
