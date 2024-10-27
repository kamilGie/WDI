def nowa_liczba(n, mask):
    i = liczba = 0

    while n>0:
        if mask % 2 == 0:
            pass
        else:
            liczba += ( n%10 ) * (10**i)
            i = i+1
        #end if
        mask = mask // 2
        n = n // 10
    #end while
    return liczba

n = int( input() )
for mask in range(1, 2**len( str(n) )):
    liczba = nowa_liczba(n, mask)
    if liczba % 7 == 0: print(liczba)










