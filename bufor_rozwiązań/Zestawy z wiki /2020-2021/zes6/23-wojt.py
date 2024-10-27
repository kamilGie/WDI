# CO TO JEST?



def opor(t, r, mode, val, index = 1):
    if index == len(t):
        if val == r:
            return True
        else:
            return False
    if mode == 1:              # 1 = dołącz szeregowo, -1 = dołącz równolegle
        val += t[index]
    elif mode == -1 and val != 0:
        val = (val*t[index])/(val + t[index])
    print(index, val)
    return opor(t, r, 1, val, index + 1) or opor(t, r, -1 , val, index + 1)

def opor_2(t, r, val, index = 1):
    if index == 3:
        if val[1]/val[0] == r:
            return True
        else:
            return False
    val = (val[0]*t[index] + val[1], val[1] * t[index])
    print(index, val)
    return opor_2(t, r, val, index+1,)

def main(t, r):
    for i in range(len(t)):
        for j in range(len(t)):
            for k in range(len(t)):
                if i !=j and j != k and i != k:
                    tab = [t[i], t[j], t[k]]
                    print(tab)
                    if opor(tab, r, 1, t[i]) or opor(tab, r, -1, t[i])  or opor_2(tab, r, (1, t[i])):
                        return True
    return False

#t1 = [2,3,6]
#t1 = [2,2,2,2,2,2,2]
t1 = [1,2,3,4,5,6]
r1 = int(input(">>> "))

print(main(t1, r1))