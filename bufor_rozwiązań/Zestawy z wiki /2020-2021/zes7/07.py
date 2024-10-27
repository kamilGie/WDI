# 7. Proszę napisać funkcję usuwającą ostatni element listy. Do funkcji
# należy przekazać wskazanie na pierwszy element listy.

# WARTOWNIK

class Node:
    def __init__(self, value = None):
        self.val = value
        self.next = None


def remove_last(first):
    prev = first
    while first.next != None:
        prev = first
        first = first.next

    # print_ll(first.next.next.next)
    
    # del prev.next
    prev.next = None
    

# import helper_module as hm
from helper_module import arr2list, print_ll

a = arr2list([5,64])
remove_last(a)
print_ll(a)