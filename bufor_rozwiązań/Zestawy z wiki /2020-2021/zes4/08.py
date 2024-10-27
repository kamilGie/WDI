import random


def leng_of_longest_geometric_subsequence(sequence):
    if len(sequence) <= 2:
        return len(sequence)
    

    max_leng = 1

    for x in range(len(sequence)-2):
        q = sequence[1][x+1] / sequence[0][x]
        leng = 2

        for i in range(2, len(sequence)-x):
            if sequence[i][x+i] == sequence[i-1][x+i-1]*q:
                leng += 1
            else:
                max_leng = max(max_leng, leng)
                leng = 2
                q = sequence[i][x+i] / sequence[i-1][x+i-1]
    
        max_leng = max(max_leng, leng)
    
    for y in range(len(sequence)-2):
        q = sequence[y+1][1] / sequence[y][0]
        leng = 2

        for i in range(2, len(sequence)-y):
            if sequence[y+i][i] == sequence[y+i-1][i-1]*q:
                leng += 1
            else:
                max_leng = max(max_leng, leng)
                leng = 2
                q = sequence[y+i][i] / sequence[y+i-1][i-1]
    
        max_leng = max(max_leng, leng)

    return max_leng if max_leng >= 3 else False


# n = int(input())
# seq = [random.randint(0, 100) for _ in range(n)]
# print(seq)

seq = [
    [1,2,3,4,5],
    [1,1,2,9,34],
    [2,4,9,1,27],
    [3,3,1,27,3],
    [1,1,1,16,1]
]
print(leng_of_longest_geometric_subsequence(seq))
