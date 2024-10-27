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



def czy_y_czynnikiem_pierwszym_x(y, x):
    return x % y == 0 and prime(y)


def zad22(T):
    N = len(T)

    def rek(T, i, cnt):
        nonlocal N
        if i == N-1:
            return cnt

        k = 2
        ans = float("inf")
        while i + k < N:
            if czy_y_czynnikiem_pierwszym_x(k, T[i]):
                ans = min(ans, rek(T, i + k, cnt + 1))
            k += 1

        return ans

    ans = rek(T, 0, 0)

    return ans if ans != float("inf") else -1


# Moje rozwiazanie 
# def prime_factor(n,k):
#     return n % k == 0 and prime(k)


# def zad222(T):

#     def rek(T, i, cnt):

#         if i == len(T) - 1 :
#             print( cnt )
#             return True

#         k = 2 
#         while i + k < len(T):
#             if prime_factor( T[i], k):
#                 if rek(T, i + k, cnt + 1):
#                     return True
#             else:
#                 k + 1 

#         #end while
#         return False
#     #end def rek
#     return rek(T, 0, 0)



print(zad22([14,8,6,8,9]))
# print(zad222([14,8,6,8,9]))