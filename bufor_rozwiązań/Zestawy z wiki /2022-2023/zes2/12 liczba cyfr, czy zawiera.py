def liczba_cyfr( n ):
    return int( len( str(n) ) )

def czy_zawiera( n ):
    liczba = liczba_cyfr( n )
    pom = n

    while n != 0:
        if n % 10 == liczba:
            return "Zawiera", pom
        else:
            n = n // 10
    #end while
    return "Nie zawiera", pom

n = int( input() )
print( czy_zawiera(n) )