a, b = input().split()

digits = [0]*10

for d in a:
    digits[int(d)] += 1

for d in b:
    digits[int(d)] -= 1

for i in range(10):
    if digits[i] != 0:
        print("NIE")
        break
else:
    print("TAK")