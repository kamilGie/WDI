import math


def check_if_going_to_end_is_possible(tab):
    mask = [False]*len(tab)
    mask[0] = True

    for i, elem in enumerate(tab):
        if mask[i]:

            div = 2
            while elem > 1:
                while elem%div == 0:
                    if i + div < len(tab):
                        mask[i+div] = True
                    elem //= div
                
                div += 1
    
    return mask[-1]



tab = tuple(map(int, input().split()))
print(check_if_going_to_end_is_possible(tab))
