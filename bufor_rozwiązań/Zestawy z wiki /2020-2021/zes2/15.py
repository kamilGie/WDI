import math


def get_leng(num):
    return math.floor(math.log10(num)) + 1

def check_condition(num, leng):
    sum = 0
    num_copy = num
    # print("suma koniec:", sum)
    # print("num początek:", num)


    while num_copy > 0:
        sum += (num_copy%10)**leng
        num_copy //= 10

    # print("suma koniec:", sum)
    # print("num koniec:", num)
    # print("num_copy koniec:", num_copy)

    return sum == num


i = 1
leng = 1
# 9**n + 9**n + 9**n + ... >= 9*(10**(n-1) + 10**n + ... + 10**0)
# n * 9**n >= 10**n -1
# while leng < 61:
while leng * (9 ** leng) >= 10 ** (leng - 1):
    # print("---------------")
    if check_condition(i, leng):
        print(i)
    i += 1
    leng = get_leng(i)
