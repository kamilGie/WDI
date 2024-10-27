import math


def check_if_going_to_end_is_possible(tab, i=0):
    # print("------------")
    if i >= len(tab) or tab[i] <= 1:
        return False
    if  i == len(tab) - 1:
        return True
    
    # for div in range(2, int(math.sqrt(tab[i]))+1):
    divs = set()

    div = 2
    num = tab[i]
    while num > 1:
        while num % div == 0:
            divs.add(div)
            num //= div
        div += 1
    
    for div in divs:
        # if tab[i] % div == 0:
        if check_if_going_to_end_is_possible(tab, i+div):
            return True

    return False


print(check_if_going_to_end_is_possible([2,1,6,2,2,6,1,1,8], 0))

tab = tuple(map(int, input().split()))
print(check_if_going_to_end_is_possible(tab))
