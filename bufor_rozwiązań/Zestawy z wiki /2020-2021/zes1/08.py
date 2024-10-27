def isPrime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    
    i = 3
    while i**2 <= num:
        if num % i == 0:
            return False
        i += 2

    return True


print(isPrime(int(input())))