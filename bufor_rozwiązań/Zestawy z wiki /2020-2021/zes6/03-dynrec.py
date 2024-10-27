def find_min_cost(board, k):
    cost = [[float("inf")]*len(board) for _ in range(len(board))]

    find_min_cost_rekur(board, cost, 0, k, 0)

    return min(cost[-1])



def find_min_cost_rekur(board, cost_board, curr_cost, x, y):
    if y >= len(board):
        return

    curr_cost += + board[y][x]


    if cost_board[y][x] > curr_cost:
        cost_board[y][x] = curr_cost

        if x > 0:
            find_min_cost_rekur(board, cost_board, curr_cost, x-1, y+1)
    
        if x + 1 < len(board):
            find_min_cost_rekur(board, cost_board, curr_cost, x+1, y+1)
        
        find_min_cost_rekur(board, cost_board, curr_cost, x, y+1)

    


board = [
    [3,5,2,3,1,7],
    [3,2,2,0,1,67],
    [3,666,2,9,345,7],
    [2,5,66,3,1,34],
    [9,423,1111,34,421,7],
    [1,1,2,3,1,2]
]

print(find_min_cost(board, 4))