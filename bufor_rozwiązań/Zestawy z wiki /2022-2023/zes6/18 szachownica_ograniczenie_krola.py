from random import randint


def is_on_board(y,x,n):
    return x < n and y < n


def can_move_to(from_x, from_y, x, y):
    return from_x <= x and from_y <= y


def get_first(n):
    while n // 10 > 0:
        n = n // 10
    #end while
    return n % 10


def get_last(n):
    return n % 10


def can_get_to(y,x):
    global tab
    if y == 7 and x == 7: return True

    for i, j in [ (1,1), (1,0), (0,1) ]:
        if is_on_board(y + i, x + j, len(tab) ):
            first = get_first( tab[y+i][x+j] )
            last = get_last( tab[y][x] )
            if last < first:
                return can_get_to( y + i, x + j )
                # COŚ TU NIE DZIALA!!!!!!
    #end for

    return False
#end def


# for i in range(10000):
#     tab = [ [randint(1,15) for _ in range(8)] for _ in range(8) ]
#     if can_get_to(0,0): print("1")

tab =[[52, 2, 6, 2, 3, 3, 16, 5],
    [52, 2, 6, 2, 3, 3, 16, 5],
    [33, 52, 32, 34, 3, 2, 1, 6],
    [44, 2, 52, 4, 17, 13, 11, 33],
    [55, 86, 7, 52, 8, 9, 12, 76],
    [66, 3, 2, 6, 52, 96, 8, 87],
    [77, 31, 39, 76, 52, 52, 82, 22],
    [88, 6, 9, 13, 17, 28, 52, 52]]

print( can_get_to(0,0) )