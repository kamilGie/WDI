def find():
    best_num = 0
    best_counter = 0
    for start_a in range(2, 10_001):
        a = start_a
        counter = 0
        while abs(a - 1) > 0.00000001:
            a = (a % 2)*(3*a + 1) + (1-a % 2) * (a/2)
            counter += 1
        if counter > best_counter:
            best_counter = counter
            best_num = start_a
    return best_num


print(find())