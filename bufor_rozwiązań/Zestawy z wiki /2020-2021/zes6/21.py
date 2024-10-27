def rek(t, y, curr_sum, target_sum, not_empty = False, columns = set()):
    if y == len(t):
        return curr_sum == target_sum and not_empty

    # print(curr_sum, y, columns)

    for x in range(len(t[y])):
        if x in columns:
            continue

        # print("next column:", x)
        if rek(t, y+1, curr_sum, target_sum, not_empty, {*columns}) or \
            rek(t, y+1, curr_sum+t[y][x], target_sum, True, {*columns, x}):
            return True

    return False

arr = [
    [1,4,7],
    [12,8,4],
    [123,8,42]
]

print(rek(arr, 0, 0, 24))
