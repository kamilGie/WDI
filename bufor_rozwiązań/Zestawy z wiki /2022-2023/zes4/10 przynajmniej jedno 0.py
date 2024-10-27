def zero_check(tab):
    n = len(tab)
    column = [ 0 for i in range(n) ]

    for y in range(n):
        flag = False
        for x in range(n):
            if tab[y][x] == 0:
                flag = True
                column[x] = 1
            #end if
        #end for 2
        if not flag: return False
        else: flag = True
    #end for 1

    for element in column:
        if element == 0: return False
    #end for
    return True

tab = [ [1,2,3,0],
        [120,0,96,0],
        [8,13,0,9],
        [0,9503,0,140]]

print( zero_check(tab) )



