import math

def is_prime(num):
    if num < 2:
        return False
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    
    for i in range(6, int(num**0.5) + 1, 6):
        if num % (i-1) == 0 or num % (i+1) == 0:
            return False
    
    return True



def rek(num, p=0, alr_del = False):
    if num < 10:
        return
    # l = int(math.floor(math.log10(num)))
    if p >= int(math.floor(math.log10(num))+1):
        # print("p exit")
        # print("p:", p)
        return

    if alr_del and is_prime(num):
        print(num)
    
    rek(num, p+1, alr_del)

    # print("num", num)
    # print("p", p)
    el1 = num // (10**(p+1))*(10**(p))
    el2 = (num % (10**p))
    el = el1+el2
    # print("el1", el1)
    # print("el2", el2)
    # print("el", el)
    # print()
    rek(el, p, True)

n = 1611
rek(n)