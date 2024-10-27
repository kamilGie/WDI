def geometric_series( tab ):
    n = len(tab)
    g_counter = 0
    i = 1
    leng = 1

    while i < n-1:
        try:
            q = round( tab[i] / tab[i-1], 5)
        #end try
        except ZeroDivisionError:
            while tab[i] == 0:
                i += 1
                leng += 1
            #end while
            if leng >= 3: g_counter += 1





tab = [0,0,0,0,1,2,4,8,1,3,9]
print( geometric_series(tab) )








