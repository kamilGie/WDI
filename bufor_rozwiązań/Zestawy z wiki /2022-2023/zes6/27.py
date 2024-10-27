def przeciecie(K1,K2):
    return True

def pole(K1,K2):

    return 0

def zad27(T):
    
    def rek(T,i,cnt,P, area):
        if area > 2012:
            return False
        if cnt == 13:
            if area == 2012:
                return True
            return False
        if i == len(T):
            return False
        
        for j in range(cnt):
            if przeciecie(T[i], T[P[j]]):
                break
        else: 
            if rek(T,i+1,cnt,P,area):
                return True
            else: 
                P[cnt] = i
                return rek(T, i+1, cnt+1, P, area + pole(T[i]))
        return rek(T,i+1,cnt,P,area)
    rek(T,0,0,[0]*13, 0)