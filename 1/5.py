n = int(input("wprowadz liczbe do spierwiastkowania calkowicie"))

x = 0
a = 0
while x + (a + 1) * 2 - 1 <= n:
    a += 1
    x += a * 2 - 1

print(int(a))
