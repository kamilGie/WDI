moves = ((1, 2), (-1, 2), (1, -2), (-1, -2),
         (2, 1), (2, -1), (-2, 1), (-2, -1))



def t_print(t):
    for i in range(len(t)):
        for j in range(len(t)):
            print(t[i][j], end='\t')
        print('')
    print()

from time import sleep

def rek(board, x=0, y=0, i=0):
    t_print(board)
    sleep(1)

    if board[y][x] == -1:
        board[y][x] = i
    else:
        return False
    
    if i == len(board)**2 - 1:
        print(i)
        t_print(board)
        return True
    
    for x_m, y_m in moves:
        if x+x_m >= 0 and x+x_m < len(board) and y+y_m >= 0 and y+y_m < len(board):
            stop = rek(board, x+x_m, y+y_m, i+1)
            if stop:
                return True
        
    board[y][x] = -1

    return False



n = 5
board = [[-1]*n for _ in range(n)]
print(rek(board))



t_print(board)