def is_in_fib(a):
    f1 = f2 = k1 = k2 = 1
    sum = 0

    while sum < a:
        sum += f1
        f1, f2 = f2, f1 + f2

    while sum > a:
        sum = sum - k1
        k1, k2 = k2, k1 + k2

    return (sum == a)

def next_not_in(n):
    k = n + 1
    while True:
        if is_in_fib( k ): k = k + 1
        else: return k
    #end while

n = int( input() )
print( next_not_in(n) )