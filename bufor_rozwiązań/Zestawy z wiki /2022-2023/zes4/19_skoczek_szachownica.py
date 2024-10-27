def skoczek(tab, k):
    n = len(tab)
    counter = 0

    for y in range(n):
        for x in range(n):
            if ( y + 1 < n ) and ( x + 2 < n ):
                iloczyn = tab[y][x] * tab[y+1][x+2]
                if iloczyn == k: counter += 1

            if ( y + 2 < n ) and ( x + 1 < n ):
                iloczyn = tab[y][x] * tab[y + 2][x + 1]
                if iloczyn == k: counter += 1

            if ( y + 1 < n ) and ( x - 2 >= 0 ):
                iloczyn = tab[y][x] * tab[y + 1][x - 2]
                if iloczyn == k: counter += 1

            if ( y + 2 < n ) and ( x - 1 >= 0 ):
                iloczyn = tab[y][x] * tab[y + 2][x - 1]
                if iloczyn == k: counter += 1

        #end for 2
    #end for 1

    return counter

# --- main

def is_on_board(T, y, x):
    if 0 <= y < len(T):
        if 0 <= x < len(T):
            return True
    #end if
    return False

#end def is_on_board 

def zad19(T, k):
    n = len( T )
    cnt = 0

    for y in range( n ):
        for x in range( n ):
            jumps = [ (1,2), (2,1), (1,-2), (2,-1) ]

            for ele in jumps:
                if is_on_board(T, y + ele[0], x + ele[1] ):
                    if T[y][x] * T[ y + ele[0] ][ x + ele[1] ] == k:
                        cnt += 1 
            #end for
        #end for x  
    #end for y 
    return cnt 
#end def zad 19






tab = [ [1,2,3,4],
        [5,6,7,8],
        [9,36,2,15],
        [15,15,64,16] ]



print( skoczek(tab, 7) )
print( zad19(tab, 7) )
print()


print( skoczek(tab, 15) )
print( zad19(tab, 15) )
print()


print( skoczek(tab, 3) )
print( zad19(tab, 3) )
print()


print( skoczek(tab, 8) )
print( zad19(tab, 8) )
print()


