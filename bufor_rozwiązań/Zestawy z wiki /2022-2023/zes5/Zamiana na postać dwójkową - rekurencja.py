def bin(n):
    if n > 0:
        bin( n // 2)
        print( n % 2, end='')
    #end if
#end def



x = int( input() )
bin( x )
