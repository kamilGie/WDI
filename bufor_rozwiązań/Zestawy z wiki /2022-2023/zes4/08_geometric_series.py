# do poprawienia
# do zrobienia


# def geometric_series(tab):
#     n = len(tab)
#     best = 0

#     for i in range(0, n-1):
#         counter = 2
#         y = 1
#         q = round( tab[y][i+1] / tab[y-1][i], 5 )
#         i += 1

#         for j in range(i+1, n):
#             if round(tab[j][y+1] / tab[i][y], 5) == q:
#                 counter += 1
#                 y += 1
#             else:
#                 break
#         #end for 2
#         best = max(best, counter)
#     #end for 1
#     return max(best, counter)



# tab = [ [1,2,3,4], 
#         [5,6,7,8], 
#         [9,10,36,12], 
#         [13,14,15,216]]

# print( geometric_series(tab) )

def geometric_series(T):
    max_leng = 1

    for x in range( len(T) - 2 ):
        q = T[1][x+1] / T[0][x] 
        leng = 2 

        for i in range(2, len(T) - x): # i - wiersze 

            if T[i][x+i] == T[i-1][x + i - 1] * q:
                leng += 1
            
            else:
                max_leng = max(max_leng, leng)
                q = T[i][x+i] / T[i-1][x + i - 1]
            
        max_leng = max(max_leng, leng)
    #end for 1



    for y in range( len(T) - 2 ):
        q = T[y+1][1] / T[y][0]
        leng = 2

        for i in range(2, len(T) - y):

            if T[y+i][i] == T[y+i-1][i-1] * q:
                leng += 1

            else:
                max_leng = max(max_leng, leng)
                leng = 2
                q = T[y+i][i] / T[y+i-1][i-1]
        max_leng = max(max_leng, leng)
    #end for 2
    return max_leng if max_leng >= 3 else False 
#end def --------



T= [ [1,2,3,4], 
     [5,6,7,8], 
     [9,10,36,12], 
     [13,14,15,216]]

print( geometric_series(T) )
