# 16. Proszę napisać funkcję, która otrzymując jako parametr wskazujący na początek listy
# jednokierunkowej, przenosi na początek listy te z nich, które mają parzystą ilość piątek w zapisie
# ósemkowym.


from helper_module import print_ll, Node, arr2list, push_front
from time import sleep

def no_of_5s_in_oktal_even(num):
    counter = 0

    while num > 0:
        if num % 8 == 5:
            counter += 1
        num //= 8
    
    return counter % 2 == 0


def solve(l):
    start = l # used to push elements front

    if l.next == None:
        return

    if no_of_5s_in_oktal_even(l.next.val): # used to avoid infinity loop if first elem passes check
        l = l.next

    while l != None and l.next != None:

        curr_val = l.next.val

        if no_of_5s_in_oktal_even(curr_val):
            push_front(start, curr_val)

            l.next = l.next.next
        else:
            l = l.next


a = arr2list([2,6,1,5,10,4,12])
# a = arr2list([5,4,7,4353,234,5,5,5,2342,5,77,5])
solve(a)
print_ll(a)