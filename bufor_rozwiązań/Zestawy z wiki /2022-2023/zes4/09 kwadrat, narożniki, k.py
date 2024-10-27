# IDK czy dobrze to jest ???
def kwadrat(tab, k):
    bok = 3
    n = len(tab)

    for y in range(n):
        for x in range(n):
            while ( y + bok <= n ) and ( x + bok <= n ):
                    iloczyn = tab[y][x] * tab[y][x+bok-1] * tab[y+bok-1][x] * tab[y+bok-1][x+bok-1]
                    if iloczyn == k:
                        print( (2*y+bok-1)//2, (2*x+bok-1)//2)
                        return True
                    #end if
                    bok += 2
            #end while
            iloczyn = 1
            bok = 3
    #end for

    return False

# tab = [ [1,2,3,4],
#         [5,6,7,8],
#         [9,10,11,12],
#         [13,14,15,16] ]

tab = [
    [1,2,4,2,1,3],
    [3,2,56,7,7,4],
    [1,2,7,2,1,3],
    [2,3,5,1,3,0],
    [3,2,56,7,7,4],
    [4,6,2,3,45,6]
]

k = int(input())
print( kwadrat(tab, k) )


def zad9(T, k):
    n = len(T)

    for y in range(n):
        for x in range(n):
            bok = 2
            iloczyn = 1
            while y + bok < n and x + bok < n:
                iloczyn = T[y][x] * T[y+bok][x] * T[y][x+bok] * T[y+bok][x+bok]

                if iloczyn == k:
                    return (y + y + bok ) // 2, ( x + x + bok ) // 2
                #end if
                bok += 2 
            #end while
    #end for y
    return False 
#end def 
                

T = [ [1,2,3,4,5], 
      [5,6,7,8,3], 
      [9,10,11,12,4], 
      [13,14,15,16,1],
      [4, 3, 5, 3, 1] ]

print( zad9(T, 297 ))



