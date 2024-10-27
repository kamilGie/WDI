n = int( input() )

unikalna_cyfra = n % 10
n = n // 10

while n > 0:
    if n%10 == unikalna_cyfra:
        print("Nie jest")
        break
    else:
        n = n // 10
else:
    print("Jest")
