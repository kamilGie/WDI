def is_prime(num):
    if num == 2 or num == 3:
        return True
    if num <= 1 or num%2 == 0 or num%3 == 0:
        return False

    for i in range(6, int(num**0.5) + 1, 6):
        if num%(i-1) == 0 or num%(i+1) == 0:
            return False
    return True


print(is_prime(57))
