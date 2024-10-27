def NWD(a,b):
    while b>0:
        a, b = b, a%b
    #end while
    return a



a = int( input() )
b = int( input() )
c = int( input() )

print( NWD( NWD(a,b), c ) )


