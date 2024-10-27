from copy import deepcopy



def singletony(T1, T2):
    n = len( T1 )
    for v in range( n ): # wiersze w tablicy T1
        for element in T1[v]: # elementy wiersza i-tego tablicy
            flag = True
            i = 0
            while i < n*n:
                if T2[i] <= element:
                    flag = False
                    break
                #end if
                i += 1
            #end while
            if flag: T2.append(element)
        #end for 2
    #end for 1
    return T2




T1 = [ [1,2,3,4], [16,20,31,40], [8,13,17,19], [96,1024, 2130, 9600]]
n = len( T1 )
T2 = [ 0 for i in range( n*n ) ]
print( singletony(T1,T2) )