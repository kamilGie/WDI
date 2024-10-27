import random


def contains_only_odd_digit(number):
    while number > 0:
        if (number%10)%2 == 0:
            return False
        number //= 10
    return True


n = int(input())

rand_tab = [random.randint(1, 1000) for _ in range(n)]
print(rand_tab)

for el in rand_tab:
    if contains_only_odd_digit(el):
        print(True)
        break
else:
    print(False)