from math import sqrt


def prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0 or n <= 1:
        return False
    i = 5
    while i <= sqrt(n) + 1:
        if n % i == 0:
            return False
        i += 2
        if n % i == 0:
            return False
        i += 4
    # end while
    return True


def zad5(T):
  def rek(T, i, x, k):
    x *= 2
    x += T[i]

    if i - k + 1 > 30:
      return False

    if i == len(T)-1:
      if prime(x):
        return True
      return False

    if prime(x):
      return rek(T, i+1, 0, i+1) or rek(T, i+1, x, k)
    return rek(T, i+1, x, k)

  return rek(T, 0, 0, 0)


  
def bin_to_dec(T,k,i):
    x = 0
    pom = 0
    for y in range(i,k-1,-1):
        x += T[y] * ( 2 ** pom )
        pom += 1
    #end for
    return x 


# Niekoniecznie dobrze

# def zad52(T):
#     def rek(x,k,i): # x - tworzona liczba, k - miejscie ciecia, i - indeks w tablicy
#         if i == len(T):
#             if prime(x): return True 
#             return False 
        
#         elif i - k + 1 > 30: 
#             return False 
        
#         else:
#             if prime(x):
#                 return rek(0,i+1,i+1) or rek(bin_to_dec(T,k,i),k,i+1)
#             else:
#                 return rek(bin_to_dec(T,k,i),k,i+1)
#     #end def
#     return rek(0,0,0)


print( zad5([1, 1, 0, 1, 0, 0]) )
print( zad5([1,1,1,0,1,1]) )
# print( zad52([1, 1, 0, 1, 0, 0]) )
# print( zad52([1,1,1,0,1,1]) )