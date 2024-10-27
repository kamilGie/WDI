import math
import random


def is_prime(num):
    if num <= 1:
        return False
    if num == 2 or num == 3:
        return True
    if num%2 == 0 or num%3 == 0:
        return False
    
    for div in range(6, int(math.sqrt(num)) + 1, 6):
        if num%(div-1) == 0 or num%(div+1) == 0:
            return False
    
    return True



def check(tab):
    flag = False
    a1, a2 = 1, 1
    for i in range(len(tab)):
        if i == a2:
            if tab[i] == 1 or sieve[tab[i]]:
                # print(tab[i])
                # print(i)
                return False

            a1, a2 = a2, a1+a2
        elif not flag:
            # print(tab[i])
            # print(sieve[tab[i]])
            flag = sieve[tab[i]]
    
    return flag


tab = [random.randint(1, 100) for _ in range(100)]


# tab = [1,45,27,6,43,98,3]

max_a = max(tab)

sieve = {i:True for i in range(2, max_a+1)}

for i in sieve:
    
    elem = i*2
    while elem <= max_a:
        # print(elem)
        sieve[elem] = False
        elem += i
sieve[1] = False
# print("--------------")
# primes = {elem for elem, prime in sieve.items() if prime}


print(tab)
print(check(tab))
            

    
