import math


def sum_of_digits(num):
    s = 0
    while num > 0:
        s += num % 10
        num //= 10
    return s



def is_smith_number(num):
    # print("----")
    digits_of_divs_sum = 0
    digits_of_num_sum = sum_of_digits(num)
    # print("=========")
    for div in range(2, num//2 + 1):
        if num % div == 0:
            digits_of_div_sum = sum_of_digits(div)
            while num % div == 0:
                digits_of_divs_sum += digits_of_div_sum
                num //= div

    return digits_of_divs_sum == digits_of_num_sum


# print(is_smith_number(85))
# print(is_smith_number(81))


for i in range(2, 1_000_000):
    if is_smith_number(i):
        print(i)


# for i in range(2, 1_000):
#     if is_smith_number(i):
#         print(i)
