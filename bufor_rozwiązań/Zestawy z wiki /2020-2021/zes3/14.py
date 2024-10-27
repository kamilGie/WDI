def calc_probability(n):
    k = 365
    p_prim = 1
    for i in range(n):
        p_prim *= 1-i/k
    
    return 1 - p_prim


print(calc_probability(20))
print(calc_probability(30))
print(calc_probability(40))