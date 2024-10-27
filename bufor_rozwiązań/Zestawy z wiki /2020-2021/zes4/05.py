import random


def find_max_column_to_line_ratio(tab):
    max_ratio = 0

    def calc_column_sum(tab, x):
        sum = 0
        for y in range(len(tab)):
            sum += tab[y][x]
        return sum

    column_sums = [calc_column_sum(tab, x) for x in range(len(tab))]

        
    for y in range(len(tab)):
        # column sum
        line_sum = max(tab[y])
            
        for x in range(len(tab[y])):
            if line_sum == 0:
                continue
            max_ratio = max(column_sums[x]/line_sum, max_ratio)

    return max_ratio  

n = 10
tab = [[random.randint(0, 50) for _ in range(n)] for _ in range(n)]


print(tab)
print(find_max_column_to_line_ratio(tab))