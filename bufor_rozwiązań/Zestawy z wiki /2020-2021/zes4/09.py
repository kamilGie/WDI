def find_square_of_edge_product_k(tab, k):
    for square_side_length in range(2, len(tab), 2):
        for x in range(len(tab)):
            for y in range(len(tab)):
                if x+square_side_length < len(tab) and y+square_side_length < len(tab):
                    if tab[y][x] * tab[y][x+square_side_length] * tab[y+square_side_length][x] * tab[y+square_side_length][x+square_side_length] == k:
                        return True, y+square_side_length//2, x+square_side_length//2
    
    return False


tab = [
    [1,2,4,2,1,3],
    [3,2,56,7,7,4],
    [1,2,7,2,1,3],
    [2,3,5,1,3,0],
    [3,2,56,7,7,4],
    [4,6,2,3,45,6]
]

print(find_square_of_edge_product_k(tab, 16))