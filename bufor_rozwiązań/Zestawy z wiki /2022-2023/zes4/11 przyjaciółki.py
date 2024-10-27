

def same_digits(a,b):
    T1 = [0] * 10
    T2 = [0] * 10

    while a > 0:
        T1[ a % 10 ] = 1
        a = a // 10
    #end while

    while b > 0:
        T2[ b % 10 ] = 1
        b = b // 10
    #end while


    return T1 == T2
#end def 

def skrajne(tab):
    n = len(tab) - 1
    counter = 0
    if same_digits(tab[0][0], tab[0][1]):
        if same_digits( tab[0][0], tab[1][0]): counter += 1

    if same_digits( tab[0][n], tab[0][n-1]):
        if same_digits( tab[0][n], tab[1][n]): counter += 1

    if same_digits(tab[n][0], tab[n-1][0]):
        if same_digits(tab[n][0], tab[n][1]): counter += 1

    if same_digits(tab[n][n], tab[n][n-1]):
        if same_digits(tab[n][n], tab[n-1][n]): counter += 1

    return counter


def friends(tab):
    counter = skrajne(tab)
    n = len(tab)

    for i in range(1, n-1): # pas u samej góry
        if same_digits( tab[0][i], tab[0][i-1] ): # [0][i-1], [0][i+1], [1][i] oraz [0][i]
            if same_digits( tab[0][i], tab[1][i] ):
                if same_digits( tab[0][i], tab[0][i+1] ):
                    counter += 1
    #end for 1

    for i in range(1, n-1): # pas na samym dole
        if same_digits( tab[n-1][i], tab[n-1][i-1] ):
            if same_digits( tab[n-1][i], tab[n-1][i+1] ):
                if same_digits( tab[n-1][i], tab[n-2][i] ):
                    counter += 1
    #end for 2

    for i in range(1, n-1): # pas po lewej stronie
        if same_digits( tab[i][0], tab[i-1][0] ):
            if same_digits( tab[i][0], tab[i][1] ):
                if same_digits( tab[i][0], tab[i+1][0] ):
                    counter += 1
    #end for 3

    for i in range(1, n-1): # pas po prawej stronie
        if same_digits( tab[n-1][i], tab[n-1][i-1] ):
            if same_digits( tab[n-1][i], tab[n-2][i] ):
                if same_digits( tab[n-1][i], tab[n-1][i+1] ):
                    counter += 1
    #end for 4

    for y in range(1, n-1):
        for x in range(1,n-1):
            if same_digits( tab[y][x], tab[y-1][x] ):
                if same_digits( tab[y][x], tab[y][x+1] ):
                    if same_digits( tab[y][x], tab[y+1][x+1] ):
                        if same_digits( tab[y][x], tab[y][x-1] ):
                            counter += 1
    #end for 5

    return counter


### SUPER SPOSÓB
def same_digits(a,b):
    T1 = [0] * 10
    T2 = [0] * 10

    while a > 0:
        T1[ a % 10 ] = 1
        a = a // 10
    #end while

    while b > 0:
        T2[ b % 10 ] = 1
        b = b // 10
    #end while

    return T1 == T2
#end def 

def is_on_board(T, y, x):
    if 0 <= y < len(T):
        if 0 <= x < len(T):
            return True
    #end if
    return False

#end def is_on_board 


def zad11(T):
    cnt = 0
    n = len( T )

    for y in range( n ):
        for x in range( n ):
            flag = True
            jumps = [ (-1,-1), (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1) ]
            for ele in jumps:
                if is_on_board( T, y + ele[0], x + ele[1] ):
                    if not same_digits( T[y][x], T[ y + ele[0] ][ x + ele[1] ] ):
                        flag = False 
                        break
                    #end if 2
                #end if 1
            #end for x
            if flag == True: cnt += 1  
    #end for y 

    return cnt
#end def zad11

T = [ [321,132,1312,0],
      [3333221,1223,7,0],
      [9,10,0,12],
      [13,14,0,16] ]


print( zad11(T) )

####
tab = [ [11,111,3,4],
        [11,19,19,60],
        [19,91,919,600],
        [91, 19, 60,6000]]

print( friends(tab) )
