# back tracking, jeśl znajdziemy się w punkcie, gdzie nie mamy możliwości skoku ponownie, to wracamy do poprzedniego i szukamy innej drogi

def knight_chess(T, w = 0, k = 0, n = 1):
    T[w][k] = n

    if n == len(T) ** 2:
        return True
    #end if


    jumps = [ (-2,-1), (-1,2), (1,2), (2,1), (2,-1), (1,-2), (-1,-2), (-2,1) ]
    for jump in jumps:
        next_w = w + jump[0]
        next_k = k + jump[1]
        if jump_is_possible(T, next_w, next_k ) and T[next_w][next_k] == 0:
            if knight_chess(T, next_w, next_k, n + 1 ):
                return True
            #end if 2
        #end if 1
    #end for
    T[w][k]=0
    return False
#end def function


def jump_is_possible(T, next_w , next_k):
    if 0 <= next_w < len(T) and 0 <= next_k < len(T): return True
    return False
#end def

def if_jump_possible(T,y,x):
    n = len(T)
    if 0 <= y < len(T):
        if 0 <= x < len(T):
            return True
    #end if
    return False 

def zad4(T):
    def rek(y,x,i):
        T[y][x] = i 
        if i == len(T) ** 2 :
            return True 
        else:
            jumps = [ (-1,-2), (-2,-1), (-2, 1), (-1,2), (1,2), (2,1), (2,-1), (1,-2) ]
            for jump in jumps:
                if if_jump_possible( T, y+jump[0], x+jump[1] ) and T[y+jump[0]][x+jump[1]] == 0:
                    if rek(y+jump[0], x+jump[1], i + 1):
                        return True 
            #end for
            T[y][x] = 0
            return False 
    #end def rek 
    print(rek(0,0,1))
#end zad4

T2 = [ [0 for _ in range(5) ] for _ in range(5) ]
# print( knight_chess(T2) )
zad4(T2)
for row in T2:
    print(row)
