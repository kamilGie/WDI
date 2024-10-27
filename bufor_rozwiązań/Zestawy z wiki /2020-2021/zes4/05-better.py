import random


def find_max_column_to_line_ratio(tab):
    # max_ratio = 0
    # max_ratio_x = 0
    # max_ratio_y = 0

    def calc_column_sum(tab, x):
        sum = 0
        for y in range(len(tab)):
            sum += tab[y][x]
        return sum

    column_sums = [calc_column_sum(tab, x) for x in range(len(tab))]
    row_sums = [sum(tab[y]) for y in range(len(tab))]

    max_col = max(column_sums)
    min_col = min(column_sums)
    index_max_col = column_sums.index(max_col)
    index_min_col = column_sums.index(min_col)
    
    max_row = max(row_sums)
    min_row = min(row_sums)
    index_max_row = row_sums.index(max_row)
    index_min_row = row_sums.index(min_row)

    ans_ratio = max_col/min_row

    return max_col/min_row, index_max_col, index_min_row


n = 10
tab = [[random.randint(1, 50) for _ in range(n)] for _ in range(n)]
tab = [[91, 68, 92], [87, 61, 96], [73, 77, 53]]

def print_tab(tab):
	for line in tab:
		print(line)
	print("--------------")

print_tab(tab)
print(find_max_column_to_line_ratio(tab))