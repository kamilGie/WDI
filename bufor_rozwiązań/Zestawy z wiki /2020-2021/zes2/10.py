def next_a(a):
    return 3*a + 1

num = int(input())

a = 2
while a <= num:
    if num%a == 0:
        print(True)
        break
    a = next_a(a)
else:
    print(False)