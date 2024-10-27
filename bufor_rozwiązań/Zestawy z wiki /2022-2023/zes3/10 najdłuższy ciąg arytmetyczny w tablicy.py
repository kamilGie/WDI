def longest_series(tab):
    best_length = 2
    counter = 2

    r = tab[1] - tab[0]
    for i in range(2, len(tab) ):
        if tab[i] - tab[i-1] == r:
            counter += 1
        else:
            best_length = max(counter, best_length)
            counter = 2
            r = tab[i]-tab[i-1]
        #end if
    #end for
    return max(best_length, counter)


tab = [1, 2, 3, 4, 5, 6, 7, 0, 5, 10, 15, 20,25,30,35,40]
if len( tab ) == 0: print(0)
elif len( tab) == 1: print(1)
else: print( longest_series(tab) )