def dec_to(n , s):
    t = [0 for i in range(64) ]
    index = 0

    while n > 0:
        t[index] = n % s
        n = n // s
        index += 1
    #end while
    for j in range(index-1, -1, -1):
        print("0123456789ABCDEF"[ t[j] ], end="")

# n = int( input() )
# s = int( input() )
# dec_to(n, s)
for i in range(1,10,-1):
    print(i)