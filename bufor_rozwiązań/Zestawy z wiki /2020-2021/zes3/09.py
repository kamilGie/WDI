import random


def leng_of_longest_increasing_subsequence(sequence):
    if len(sequence) <= 1:
        return len(sequence)
    
    max_leng = 1
    leng = 1
    for i in range(1, len(sequence)):
        if sequence[i-1] < sequence[i]:
            leng += 1
        else:
            max_leng = max(max_leng, leng)
            leng = 1
    
    return max_leng


n = int(input())
seq = [random.randint(0, 100) for _ in range(n)]
print(seq)
print(leng_of_longest_increasing_subsequence(seq))
