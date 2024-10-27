def increasing_number(num):
    a = num % 10
    num //= 10
    while num > 0:
        if a <= num % 10:
            return False
        a = num % 10
        num //= 10
    return True


n = int(input())

print(increasing_number(n))