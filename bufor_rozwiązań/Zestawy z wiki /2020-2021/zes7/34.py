# 34. Proszę napisać funkcję, która usuwa z listy cyklicznej elementy, których klucz występuje
# dokładnie k razy. Do funkcji należy przekazać wskazanie na jeden z elementów listy, oraz liczbę k,
# funkcja powinna zwrócić informację czy usunięto jakieś elementy z listy.

from helper_module import Node, print_ll, arr2list


def solve(cycle, k):
    if k == 0:
        return False

    abs_start = cycle
    if cycle.val == None:
        cycle = cycle.next
    
    start = cycle
    counter = {}

    counter[cycle.val] = 1
    cycle = cycle.next

    while cycle != start:
        counter[cycle.val] = counter.get(cycle.val, 0) + 1
        cycle = cycle.next
    
    removed = False
    while cycle.next != start:
        if counter[cycle.next.val] == k:
            cycle.next = cycle.next.next
            removed = True
        else:
            cycle = cycle.next
    

    if cycle.next == start and counter[cycle.next.val] == k:
        cycle.next = cycle.next.next
        removed = True

    abs_start.next = cycle

    return removed


a = arr2list([5,7,3,4,4,8,4,7])
a.next.next.next.next.next.next.next.next.next = a.next

print(solve(a, 1))
print_ll(a)