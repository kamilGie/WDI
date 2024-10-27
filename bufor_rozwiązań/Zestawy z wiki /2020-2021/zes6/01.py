def c_sieve(limit):
    s = set()
    primes = set()
    for i in range(2, limit+1):
        if i in s:
            continue
        
        primes.add(i)

        for j in range(i*2, limit+1, i):
            s.add(j)
        
    return primes


def recur(num_str, memory: set):
    if len(num_str) < 2:
        return 0
    
    if num_str in memory:
        return 0
    
    memory.add(num_str)

    for i in range(len(num_str)):
        recur(num_str[:i]+num_str[i+1:], memory)


def check(num):
    mem = set()
    num = str(num)
    primes = c_sieve(10**(len(num)))

    recur(num, mem)

    ans = {cand for cand in mem if int(cand) in primes}
    return ans


print(check(1234))

