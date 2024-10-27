
opcje = 0
def hetmany():
    
    def rek(K, i):
        global opcje
        if i == 8:
            opcje += 1
            print(K)
        else:
            for x in range(8):
                j = 0
                while j < i:
                    if K[j] == x or abs(K[j] - x) == i - j:
                        break
                    j += 1
                else:
                    K[i] = x
                    rek(K, i+1)

    rek([0]*8, 0)


hetmany()
print(opcje)
