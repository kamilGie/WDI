# n = int(input())
n = 100

sieve = [i for i in range(n)]
sieve[0] = False
sieve[1] = False

for i in range(2, n):
    if sieve[i] > 0:
        for j in range(2*sieve[i], n, sieve[i]):
            sieve[j] = 0

for el in sieve:
    if el > 0:
        print(el, end=" ")
print()