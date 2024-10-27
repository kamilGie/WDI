import math

def is_prime(num):
    if num < 2:
        return False
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    
    for i in range(6, int(num**0.5) + 2, 6):
        if num % (i-1) == 0 or num % (i+1) == 0:
            return False
    
    return True


primes = 0

def rek(num1, num2, new_num=0, power=1):
    # print(new_num)
    if num1 == 0 and num2 == 0:
        if is_prime(new_num):
            print("PRIME:", new_num)
            global primes
            primes += 1
        return


    if num1 > 0:
        rek(num1//10, num2, (num1%10)*power+new_num, power*10)
    if num2 > 0:
        rek(num1, num2//10, (num2%10)*power+new_num, power*10)


rek(2, 11)
print(primes)
