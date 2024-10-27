from random import randint


# Dana jest tablica T[N] zawierająca liczby naturalne. Proszę napisać funkcję, która odpowiada
# na pytanie, czy spośród (niekoniecznie wszystkich) elementów tablicy można utworzyć dwa podzbiory o
# jednakowej sumie elementów, tak aby suma mocy obu podzbiorów wynosiła k. Do funkcji należy przekazać
# wyłącznie tablicę T oraz liczbę naturalną k, funkcja powinna zwrócić wartość typu bool


def zad32(T, k):
    
    def rek(T, k, i, X,Y,x_size, y_size):
        if x_size + y_size == k:
            x_sum, y_sum = 0, 0
            for j in range(x_size):
                x_sum += X[j]
            for k in range(y_size):
                y_sum += Y[k]
            return x_sum==y_sum

        if i == len(T):
            return False

        if x_size==k-1:
            if rek(T, k, i+1, X,Y,x_size, y_size):
                return True
            Y[y_size] = T[i]
            return rek(T,k, i+1, X, Y, x_size, y_size+1)
        
        if y_size==k-1:
            if rek(T, k, i+1, X,Y,x_size, y_size):
                return True
            X[x_size] = T[i]
            return rek(T,k, i+1, X, Y, x_size+1, y_size)

        X[x_size] = T[i]
        Y[y_size] = T[i]
        return rek(T, k, i+1, X,Y,x_size, y_size) or rek(T,k,i+1, X,Y, x_size+1, y_size) or rek(T, k, i+1, X,Y,x_size, y_size+1)

    #end def
    return rek(T,k,0,[0]*(k-1), [0]*(k-1), 0, 0)


def zadanie(T,k):
    def rek(T,k,sum,cnt_a,cnt_b,i):
        if cnt_a + cnt_b == k and sum == 0:
            return True
        if i == len(T):
            return False
        else:
            return rek(T,k,sum+T[i],cnt_a+1,cnt_b,i+1) or rek(T,k,sum-T[i],cnt_a,cnt_b+1,i+1) or rek(T,k,sum,cnt_a,cnt_b,i+1) 
    return rek(T,k,0,0,0,0)




def zad322(T, k):

    def rek(T, k, i, a, b, suma):

        if suma == 0 and a != 0 and b != 0:
            if a + b == k:
                return True

        if i == len(T):
            return False 
        
        return rek(T, k, i + 1, a + 1, b, suma + T[i] ) or rek(T, k, i + 1, a, b + 1, suma - T[i] ) or rek(T, k, i + 1, a, b, suma)
    #end def rek

    return rek(T, k, 0, 0, 0, 0)
#end def zad32     


T = [ randint(1,20) for i in range(8) ]
print(zad32(T, 8))
print(zad322(T, 8))
print(zadanie(T,8))
print()

T = [ randint(1,20) for i in range(8) ]
print(zad32(T, 8))
print(zad322(T, 8))
print(zadanie(T,8))
print()


T = [ randint(1,20) for i in range(8) ]
print(zad32(T, 8))
print(zad322(T, 8))
print(zadanie(T,8))
print()


T = [ randint(1,20) for i in range(8) ]
print(zad32(T, 8))
print(zad322(T, 8))
print(zadanie(T,8))
print()

