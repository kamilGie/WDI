# 18. Proszę napisać funkcję, która pozostawia w liście wyłącznie elementy unikalne. Do funkcji należy
# przekazać wskazanie na pierwszy element listy.

from helper_module import print_ll, Node, arr2list, push_front, reverse_list
from time import sleep


def solve(l):
    uniques = Node()

    c1 = l.next
    while c1 != None:
        c2 = l.next
        passed = True
        while c2 != None:
            # print("c1:", c1.val, "c2:", c2.val)
            if c1 == c2:
                # print("skipped")
                c2 = c2.next
                continue

            if c1.val == c2.val:
                passed = False
                break
            c2 = c2.next

        if passed:
            push_front(uniques, c1.val)

        c1 = c1.next

    ans = Node()
    reverse_list(uniques, ans)
    # print_ll(ans)
    l.next = ans.next

        
    
a = arr2list([3,4,5,234,1,45,3,4])
# print_ll(a)
solve(a)
print_ll(a)