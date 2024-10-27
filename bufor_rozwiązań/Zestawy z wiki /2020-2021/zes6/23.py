# Zadanie 23. Dana jest tablica T[N] zawierająca oporności N rezystorów wyrażonych całkowitą liczbą
# kΩ. Proszę napisać funkcję, która sprawdza czy jest możliwe uzyskanie wypadkowej rezystancji R (równej
# całkowitej liczbie kΩ) łącząc dowolnie 3 wybrane rezystory.


def poss(t, idx, target):
    if abs(t[idx[0]] + t[idx[1]] + t[idx[2]] - target) < 0.00001:
        return True
    if abs((t[idx[0]] * t[idx[1]] * t[idx[2]])/(t[idx[0]]*t[idx[2]] + t[idx[1]]*t[idx[2]] + t[idx[2]]*t[idx[1]]) - target) < 0.00001:
        return True
    if abs(t[idx[0]] + (t[idx[1]] * t[idx[2]])/(t[idx[1]] + t[idx[2]]) - target) < 0.00001:
        return True
    if abs(t[idx[2]] + (t[idx[1]] * t[idx[0]])/(t[idx[1]] + t[idx[0]]) - target) < 0.00001:
        return True
    if abs(t[idx[0]] + (t[idx[1]] * t[idx[2]])/(t[idx[1]] + t[idx[2]]) - target) < 0.00001:
        return True
    
    x = t[idx[0]] + t[idx[1]]
    if abs((x * t[idx[2]])/(x + t[idx[2]]) - target) < 0.00001:
        return True

    x = t[idx[0]] + t[idx[2]]
    if abs((x * t[idx[1]])/(x + t[idx[1]]) - target) < 0.00001:
        return True

    x = t[idx[1]] + t[idx[2]]
    if abs((x * t[idx[0]])/(x + t[idx[0]]) - target) < 0.00001:
        return True
    

    return False


def zad(t, target):
    def rek(t, target, index=0, idx=None, no_of_resistors=0):
        idx = idx or []
        # h = h or [(t[0], "first")]

        if no_of_resistors == 3:
            # print(resistance, h, no_of_resistors)
            return poss(t, idx, target)

        if index == len(t):
            return False
        
        
        return rek(t, target, index+1, [*idx, index], no_of_resistors+1) or \
                rek(t, target, index+1, [*idx], no_of_resistors)

    return rek(t, target, 0, [0], 1) or \
        rek(t, target, 1, [1], 1)


res = [3,6,2,4,2,6,2]
print(zad(res, 1.6))