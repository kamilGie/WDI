from math import sqrt

def prime(n):
    if n == 2 or n == 3: return True
    if n <= 1 or n % 2 == 0 or n % 3 == 0: return False

    i = 5
    while i < sqrt(n) + 1:
        if n % i == 0: return False
        i += 2
        if n % i == 0: return False
        i += 4
    #end
    return True

###


def new_number_prime(a,b):

    def rek(a,b,x,i):
        if a == 0 and b == 0:
            if prime(x):
                print(x)
                return 1
            return 0
        #end if
        if a == 0:
            return rek(a,0, x + b * ( 10**i ), i + 1 )
        #end if
        if b == 0:
            return rek(0, b, x + a * ( 10**i ), i + 1 )
        #end if
        return rek( a//10, b, x + (a%10) * ( 10**i ), i + 1 ) + rek(a, b//10, x + (b%10) * (10 **i ), i + 1)
    #end def
    return rek(a,b,0,0)
#end def


# Mojego autorstwa, do dopracowania !
# def rek_2(x,y,n,i):

#     if x == 0 and y == 0:
#         if prime(n): print(n)
#         return

#     if x == 0: 
#         y = y * ( 10 ** i )
#         n = n + y 
#         if prime(n): print(n)
#         return 
    
#     if y == 0:
#         x = x * ( 10 ** i )
#         n = n + x
#         if prime(n): print(n)
#         return

    
#     rek_2(x//10, y, n + (x % 10) * ( 10 ** i ), i + 1)
#     rek_2(x, y//10, n + (y % 10) * ( 10 ** i ), i + 1)
    


# rek_2(13,255,0,0)

print( new_number_prime(13,255) )