def Zadanie_124(s):
    p = min(max(abs(x), abs(y)) for x, y in s)
    return p != 0 and (p, p) in s and (p, -p) in s and (-p, p) in s and (-p, -p) in s
