
def leng_of_longest_arythmetic_subsequence(sequence):
    if len(sequence) <= 2:
        return len(sequence)
    

    for i in range(2, len(sequence)):
        if sequence[i] == sequence[i-1]+r:
            leng += 1
        else:
            max_leng = max(max_leng, leng)
            leng = 2
            r = sequence[i] - sequence[i-1]
    

    return max(max_leng, leng)


def leng_of_longest_geometric_subsequence(sequence):
    if len(sequence) <= 2:
        raise ValueError("Za krótka tablica")
    

    q = sequence[1] / sequence[0]
    max_la = 1
    leng_la = 2
    
    r = sequence[1] - sequence[0]
    max_lg = 1
    leng_lg = 2
    for i in range(2, len(sequence)):
        if sequence[i] == sequence[i-1]*q:
            leng_lg += 1
        else:
            max_lg = max(max_lg, leng_lg)
            leng_lg = 2
            q = sequence[i] / sequence[i-1]

        if sequence[i] == sequence[i-1]+r:
            leng_la += 1
        else:
            max_la = max(max_la, leng_la)
            leng_la = 2
            r = sequence[i] - sequence[i-1]

    max_la = max(max_la, leng_la)
    max_lg = max(max_lg, leng_lg)
    if max_la > max_lg:
        ans = 1
    elif max_la < max_lg:
        ans = -1
    else:
        ans = 0


    return ans


