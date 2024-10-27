def number_split(num, j, split):

    if num == 0:
        print(split)
        return
    #end if
    if j == 0: min = 1
    else: min = split[j-1]

    for i in range(min, num + 1 ):
        split[j] = i
        number_split( num - i, j + 1, split)
        split[j] = 0
    #end for

# np. 4: 1+3, 1+1+2, 1+1+1+1, 2+2. Zauważ, że kolejne elementy sumy są nie mniejsze od poprzedniego

n = 10
number_split(n,0,[0]*n)