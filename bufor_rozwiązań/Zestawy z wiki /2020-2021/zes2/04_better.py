num = int(input())

counter = 0

num_2 = 1
while num_2 <= num:
    num_3 = num_2
    while num_3 <= num:
        num_5 = num_3
        while num_5 <= num:
            counter += 1
            num_5 *= 5
        num_3 *= 3
    num_2 *= 2


print(counter)
