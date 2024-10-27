def series(tab):
    n = len(tab)
    res = suma = 0

    for y in range(n):
        for x in range(n):
            for i in range(1,11):
                            
                if i + y < n:
                    suma = 0
                    for j in range(y, i + y + 1):
                        suma += tab[j][x]
                    res = max(res, suma)

                if i + x < n:
                    suma = 0
                    for j in range(x, i + x + 1):
                        suma += tab[y][j]
                    res = max(res, suma)
            #end for 3
        #end for 2
    #end for 1
    return res


# --- main:

tab = [ [1,2,3,4],
      [5,6,7,8],
      [9,10,11,12],
      [13,14,15,16] ]

print( series(tab) )

