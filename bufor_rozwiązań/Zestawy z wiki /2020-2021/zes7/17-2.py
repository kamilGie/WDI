# 17. Proszę napisać funkcję, która otrzymując jako parametr wskazujący na początek listy
# dwukierunkowej, usuwa z niej wszystkie elementy, w których wartość klucza w zapisie binarnym ma
# nieparzystą ilość jedynek.


from helper_module import arr2dlist, push_front, print_ll, print_back_ll, Node_d
from time import sleep

def check(num):
    counter = 0

    while num > 0:
        counter += num%2
        num //= 2
    
    return counter%2 == 1


def remove(l):
    if l.val != None:
        q = Node_d()
        q.next = l
        l = q
    
    while l.next != None:
        if check(l.next.val):
            if l.next.next != None:
                l.next.next.prev = l

            l.next = l.next.next
        else:
            l = l.next

    


a = arr2dlist([2,52,24,7,5,62,3,6])
print_ll(a)
remove(a)
print_ll(a)
print_back_ll(a)