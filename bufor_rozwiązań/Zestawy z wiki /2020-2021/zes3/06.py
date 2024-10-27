import random


def contains_odd_digit(number):
    while number > 0:
        if (number%10)%2:
            return True
        number //= 10
    return False


n = int(input())

rand_tab = [random.randint(1, 1000) for _ in range(n)]
print(rand_tab)

for el in rand_tab:
    if not contains_odd_digit(el):
        print(False)
        break
else:
    print(True)