import math


def get_leng(num, base):
    if num == 0:
        return 1
    return int(math.floor(math.log(num, base))) + 1


def is_prime(num):
    if num <= 1:
        return False
    if num == 2 or num == 3 or num == 5:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    
    for i in range(6, int(math.sqrt(num))+1, 6):
        if num % (i-1) == 0 or num % (i+1) == 0:
            return False
        i += 2

    return True


def decimal_to_base(num, base, leng):
    num_base = [0]*leng

    for i in range(len(num_base)-1, -1, -1):
        num_base[i] = num%base
        num //= base
    
    # print(num_base)
    return num_base

# print(decimal_to_base(123,3))

def create_sum(t1, t2, mask_num: int) -> int:
    s = 0
    mask = decimal_to_base(mask_num, 3, len(t1))
    
    for i in range(len(t1)):
        # print(i)
        if mask[i] == 0:
            s += t1[i]
        elif mask[i] == 1:
            s += t2[i]
        elif mask[i] == 2:
            s += t1[i]
            s += t2[i]

    return s


def ex17(t1, t2) -> int:
    counter: int = 0
    # counter2: int = 0

    for mask in range(3**len(t1)):
        s = create_sum(t1, t2, mask)
        if is_prime(s):
            counter += 1
        # counter2 += 1

    return counter
    # return counter, counter2



t1 = [1,4,52,3,5,2,35]
t2 = [33,0,93,5,12,2,5]
print(ex17(t1, t2))


t1 = [1,3,2,4]
t2 = [9,7,4,8]
print(ex17(t1, t2))


t1 = [1,2]
t2 = [9,4]
print(ex17(t1, t2))
