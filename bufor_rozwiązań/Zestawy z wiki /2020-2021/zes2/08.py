def find_the_smallest_unsumable(num):  # probably it is possible to do this faster
    num += 1
    while True:
        f1, f2 = 1, 1
        fib_suma = 0
        while fib_suma < num:
            fib_suma += f1
            f1, f2 = f2, f1+f2

        f1, f2 = 1, 1
        while fib_suma > num:
            fib_suma -= f1
            f1, f2 = f2, f1+f2
        
        if fib_suma != num:
            return num
        num += 1




num = int(input())

print(find_the_smallest_unsumable(num))