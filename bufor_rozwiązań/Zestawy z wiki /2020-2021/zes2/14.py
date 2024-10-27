# Zadanie 14. 
# Dane są dwie liczby naturalne z których budujemy trzecią liczbę. W budowanej liczbie muszą
# wystąpić wszystkie cyfry występujące w liczbach wejściowych. Wzajemna kolejność cyfr każdej z liczb
# wejściowych musi być zachowana. Na przykład mając liczby 123 i 75 możemy zbudować liczby 12375, 17523,
# 75123, 17253, itd. Proszę napisać funkcję która wyznaczy ile liczb pierwszych można zbudować z dwóch
# zadanych liczb.

import math


def is_prime(num):
    if num <= 1:
        return False
    if num == 2 or num == 3 or num == 5:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    
    for i in range(6, int(math.sqrt(num))+1, 6):
        if num % (i-1) == 0 or num % (i+1) == 0:
            return False
        i += 2

    return True


def get_leng(num):
    return math.floor(math.log10(num)) + 1


def validate_mask(leng1: int, leng2: int, mask: int):
    while mask > 0:
        if mask % 2 == 0:
            leng1 -= 1
        else:
            leng2 -= 1

        mask //= 2


    return leng1 >= 0 and leng2 == 0


def mix_numbers(a: int, b: int, mask: int):
    new_num = 0
    mult = 1

    while mask > 0 or a > 0:
        if mask % 2 == 0:
            d = a % 10
            a //= 10
        else:
            d = b % 10
            b //= 10

        mask //= 2

        new_num = d*mult + new_num
        mult *= 10

    return new_num


if __name__ == "__main__":
    print(mix_numbers(135, 24, int('01100', base=2)))

    counter = 0
    a, b = map(int, input().split())
    leng_a, leng_b = get_leng(a), get_leng(b)

    for mask in range(2**(leng_a + leng_b)):
        if validate_mask(leng_a, leng_b, mask) and is_prime(mix_numbers(a, b, mask)):
            counter += 1

    print(counter)
