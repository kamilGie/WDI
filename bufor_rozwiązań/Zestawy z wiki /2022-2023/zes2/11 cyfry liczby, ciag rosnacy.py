def czy_rosnacy( n ):
    pom = n
    temp = n % 10
    n = n // 10

    while n != 0:
        if n % 10 < temp:
            temp = n % 10
            n = n // 10
        else:
            return "Nie jest"
    #end while
    return "Jest"


n = int( input() )
print( czy_rosnacy(n) )

