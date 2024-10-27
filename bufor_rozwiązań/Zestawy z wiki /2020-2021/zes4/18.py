def max_sum(arr):
    best_sum = float("-inf")
    best_arr = []


    # for leng in range(min(11, len(arr))-1, 0, -1):
    #     print("leng:", leng)
    #     start = 0
    #     end = leng-1
    #     curr_sum = sum(arr[:leng])
    #     if best_sum < curr_sum:
    #         best_sum = curr_sum
    #         start = 0
    #         end = leng-1
    #         best_arr = arr[start:end+1]
    #     print(leng, len(arr))
    #     print(arr)

    #     for i in range(leng, len(arr)):
    #         print("in", leng, i)
    #         curr_sum += arr[i]
    #         curr_sum -= arr[i-leng]
    #         if best_sum < curr_sum:
    #             best_sum = curr_sum
    #             start = i-leng+1
    #             end = i
    #             best_arr = arr[start:end+1]

    #     arr = arr[start:end+1]
    
    # return best_sum, best_arr
    # return best_sum


print(max_sum([3,6,2,-4,67,34,-100,46,-345,7,4,23,-43,6,2]))


def calc(tab):
    best_sum = float("-inf")

    for line in tab:
        best_sum = max(best_sum, max_sum(line))
    
    for x in range(len(tab)):
        column = [tab[i][x] for i in range(len(tab))]
        best_sum = max(best_sum, max_sum(column))
    
    return best_sum


T = [
    [1,6,-2, -23,234],
    [11,26,-2, -1,4],
    [-1,-6,-2, -23,234],
    [42,6,-2, 23,24],
    [1,6,-2, 33,-4]
]

print()
print()
print(calc(T))
