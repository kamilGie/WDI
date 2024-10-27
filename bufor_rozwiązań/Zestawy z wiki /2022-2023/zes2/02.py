def ulamek( l, m, n ):
    print( l // m , end="")
    i = 1

    if l % m != 0:
        print(".", end="")
        l = l % m
        while l > 0 and n > 0:
            l = l * 10
            print( l // m, end="")
            l = l % m
            n = n - 1
        #end while
    #end if

def ulamek2(l,m,n):
    print( l//m, end="")

    if l % m != 0:
        while n > 0:
            print( l%m )
            l = l%m
            l = l * 10
            n  = n - 1

        #end while


l = int( input() )
m = int( input() )
n = int( input() )
ulamek(l,m,n)

