def count_binary_ones(num):
    ones = 0
    while num > 0:
        ones += num%2
        num //= 2
    
    return ones


def create_binary_ones_array(tab, n):
    bin_tab = [[0]*n for _ in range(n)]
    for y in range(n):
        for x in range(n):
            bin_tab[y][x] = count_binary_ones(tab[y][x])

    return bin_tab



def compare_arrays(arr1, arr2, x2, y2):
    if y2+len(arr1) < len(arr2):
        return 0
    
    same_cells = 0
    for y in range(len(arr1)):
        if x2+len(arr1[y]) < len(arr2[y]):
            return 0
        
        for x in range(len(arr1[y])):
            if arr1[y][x] == arr2[y+y2][x+x2]:
                same_cells += 1
    
    return same_cells


def find_t1_pos_inside_t2(t1, t2):
    bin_t1 = create_binary_ones_array(t1, len(t1))
    bin_t2 = create_binary_ones_array(t2, len(t2))
    print(bin_t1)
    print(bin_t2)
    for x in range(len(t2) - len(t1)+1):
        for y in range(len(t2)-len(t1) + 1):
            if 100*compare_arrays(bin_t1, bin_t2, x, y) > 33*(len(bin_t1)**2):
                return True, x, y
    
    return False


tmp = [
    [1,4,6],
    [3,7,2],
    [3,6,1]
]

tmp2 = [
    [0,1],
    [4,20]
]

print(create_binary_ones_array(tmp, 3))
print(create_binary_ones_array(tmp2, 2))

print(find_t1_pos_inside_t2(tmp2, tmp))
print(tmp)