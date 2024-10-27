# 14. Proszę napisać funkcję, otrzymującą jako parametr wskaźnik na pierwszy element listy o
# wartościach typu int, usuwającą wszystkie elementy, których wartość dzieli bez reszty wartość
# bezpośrednio następujących po nich elementów.


from helper_module import print_ll, Node, arr2list
from time import sleep

def solve(l):
    while l.next != None and l.next.next != None:
        curr_val = l.next.val
        next_val = l.next.next.val

        if next_val % curr_val == 0:
            l.next = l.next.next
        else:
            l = l.next  



a = arr2list([2,4,6,1,5,10,4,12])
solve(a)
print_ll(a)