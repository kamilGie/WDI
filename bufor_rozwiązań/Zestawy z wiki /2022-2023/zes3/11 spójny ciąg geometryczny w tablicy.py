def longest_geometric_series( tab: list ):
    counter = 2
    best_length = 2
    q = round( tab[1] / tab[0], 5)

    for i in range(2, len( tab ) ):
        if round( tab[i] / tab[i-1], 5) == q:
            counter += 1
        else:
            best_length = max( best_length, counter )
            counter = 2
            q = round( tab[i] / tab[i-1], 5)
        #end if
    #end for
    return max(best_length, counter)

# --- main
tab = [2,4,6,8,10,20,40,80,160,2,4,8,16,32]
print( longest_geometric_series(tab) )
