def NWD(a,b):
    while b>0:
        a, b = b, a%b
    #end while
    return a

def NWW(a, b):
    return ( a * b )//(NWD(a,b))

a = int( input() )
b = int( input() )
c = int( input() )

print( NWW( NWW(a,b), c) )