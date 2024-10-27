def zliczanie(T,s,n,p):
    global licznik 
    if n == 1:
        for i in range( p, len(T) ):
            if T[i] ==  s: licznik += 1
        #end for
    
    else:
        for i in range( p, len(T) ):
            if s % T[i] == 0:
                zliczanie(T, s // T[i], n - 1, i + 1)
        #end for

t = [1,2,4,8,9,10,13,3,24]
licznik = 0
zliczanie(t,24,2,0)
print( licznik )

