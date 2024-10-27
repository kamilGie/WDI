import random


def find_max_column_to_line_ratio(tab):
    # max_ratio = 0
    # max_ratio_x = 0
    # max_ratio_y = 0

    def calc_col_and_row_sum(tab):
        col_sums = [0]*len(tab)
        row_sums = [0]*len(tab)

        for x in range(len(tab)):
            for y in range(len(tab)):
                col_sums[x] += tab[y][x]
                row_sums[y] += tab[y][x]
        
        return row_sums, col_sums



    row_sums, column_sums = calc_col_and_row_sum(tab)

    max_col = max(column_sums)
    index_max_col = column_sums.index(max_col)
    
    min_row = min(row_sums)
    index_min_row = row_sums.index(min_row)

    return max_col/min_row, index_max_col, index_min_row

    # for y in range(len(tab)):
    #     # column sum
    #     line_sum = sum(tab[y])
            
    #     for x in range(len(tab[y])):
    #         if line_sum == 0:
    #             continue

    #         ratio = column_sums[x]/line_sum
    #         if ratio > max_ratio:
    #             max_ratio = ratio
    #             max_ratio_x = x
    #             max_ratio_y = y


    # return max_ratio, max_ratio_x, max_ratio_y

n = 10
tab = [[random.randint(1, 50) for _ in range(n)] for _ in range(n)]
tab = [[91, 68, 92], [87, 61, 96], [73, 77, 53]]

def print_tab(tab):
	for line in tab:
		print(line)
	print("--------------")

print_tab(tab)
print(find_max_column_to_line_ratio(tab))