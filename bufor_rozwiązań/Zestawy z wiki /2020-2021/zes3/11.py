import random


def leng_of_longest_geometric_subsequence(sequence):
    if len(sequence) <= 2:
        return len(sequence)
    

    q = sequence[1] / sequence[0]
    max_leng = 1
    leng = 2
    for i in range(2, len(sequence)):
        if sequence[i] == sequence[i-1]*q:
            leng += 1
        else:
            max_leng = max(max_leng, leng)
            leng = 2
            q = sequence[i] / sequence[i-1]
    

    return max(max_leng, leng)


# n = int(input())
# seq = [random.randint(0, 100) for _ in range(n)]
# print(seq)

seq = tuple(map(int, input().split()))
print(leng_of_longest_geometric_subsequence(seq))
