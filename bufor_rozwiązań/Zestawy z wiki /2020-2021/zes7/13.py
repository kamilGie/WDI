# 13. Proszę napisać funkcję, otrzymującą jako parametr wskaźnik na pierwszy element listy o
# wartościach typu int, usuwającą wszystkie elementy, których wartość jest mniejsza od wartości
# bezpośrednio poprzedzających je elementów.


from helper_module import print_ll, Node, arr2list
from time import sleep

def solve(l):
    l = l.next # Wartownik
    
    last_val = l.val

    while l.next.next != None:
        curr_val = l.next.val

        if curr_val < last_val:
            curr_val = l.next.next.val
            l.next = l.next.next
        

        last_val = curr_val
        l = l.next  

    if l.next.val < last_val:
        l.next = None

    # print()


a = arr2list([4,53,6645,4,563,5,34,53,646,99])
solve(a)
print_ll(a)