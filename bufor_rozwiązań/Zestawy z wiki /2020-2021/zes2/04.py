def is_two_three_five(num):
    for div in {2, 3, 5}:
        while num%div == 0:
            num //= div
    return num == 1


n = int(input())

counter = 0
for i in range(1, n+1):
    if is_two_three_five(i):
        counter += 1

print(counter)
