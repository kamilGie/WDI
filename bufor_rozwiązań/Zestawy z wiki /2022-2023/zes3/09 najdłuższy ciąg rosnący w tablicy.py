def longest_increasing_series(tab):
    counter = 1
    best_length = 2
    for i in range( 1,len(tab) ):
        if tab[i] > tab[i-1]:
            counter += 1
        else:
            best_length = max( best_length, counter )
            counter = 1
        #end if
    #end for
    return max(best_length, counter)


tab = [1,2,3,4,3,4,5,6,7]
print( longest_increasing_series(tab) )