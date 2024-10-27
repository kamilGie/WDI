import math


def rek(t, i, s_el=0, s_it=0, best=math.inf, l=0, s_best=0):
    if i >= len(t):
        # print(s_el == s_it, s_el)
        return s_el == s_it and s_el > 0, s_el, l
    
    s_best = 0
    poss = False

    ans, s, leng = rek(t, i+1, s_el, s_it, best, l)
    if ans and leng < best:
        best = leng
        s_best = s
        poss = True
    
    ans, s, leng = rek(t, i+1, s_el+t[i], s_it+i, best, l+1)
    if ans and leng < best:
        best = leng
        s_best = s
        poss = True
    
    return poss, s_best, best


t = [1,7,3,5,11,2]

print(rek(t, 0))

