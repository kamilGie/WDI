def solve(t, r):
    if len(t) < 3:
        return False

    def rek(t, r, indexes, curr_i):
        if len(indexes) == 3:
            c_x = (t[indexes[0]][0]+t[indexes[1]][0]+t[indexes[2]][0])/3
            c_y = (t[indexes[0]][1]+t[indexes[1]][1]+t[indexes[2]][1])/3
            c_z = (t[indexes[0]][2]+t[indexes[1]][2]+t[indexes[2]][2])/3

            if c_x**2 + c_y**2 + c_z**2 <= r**2:
                return True
            return False

        if curr_i == len(t):
            return False

        return rek(t, r, [*indexes, curr_i], curr_i+1) or \
            rek(t, r, [*indexes], curr_i+1)
    
    return rek(t, r, [], 0)


arr = [
    (4,1,2), 
    (4,6,1),
    (1,8,8), 
    (4,8,8),
    (4,8,2), 
    (1,1,1)
]

R = 5
print(solve(arr, R))