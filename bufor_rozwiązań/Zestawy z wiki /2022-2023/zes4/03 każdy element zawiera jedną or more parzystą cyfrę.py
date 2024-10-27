def at_least_one_even(n):
    temp = n
    while temp!= 0:
        if ( temp % 10 ) % 2 == 0: return True
        temp = temp // 10
    #end while
    return False



def even_in_verse(tab):
    for element in tab:
        if not at_least_one_even( element ): return False
    #end for
    return True


def check_tab_for_even_verses(tab):
    for i in tab:
        if even_in_verse( i ): return True
    #end for
    return False


tab = [ [12,2,413], [4,52,333], [333,230,58198] ]
print( check_tab_for_even_verses(tab) )




