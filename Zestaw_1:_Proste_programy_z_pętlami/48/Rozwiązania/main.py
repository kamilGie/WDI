# ====================================================================================================>
# Zadanie 48
# Proszę napisać program wyznaczający najmniejszą liczbę pierwszą o sumie cyfr równej N,
# której cyfry są w porządku rosnącym
# ====================================================================================================>


def is_prime(num):
    if num < 2:
        return False
    if num in (2, 3):
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True


def Zadanie_48(N):
    for number in range(10 ** (N // 9), 10**N):
        digits = list(map(int, str(number)))
        if sum(digits) == N and digits == sorted(digits):
            if is_prime(number):
                return number
    return None


