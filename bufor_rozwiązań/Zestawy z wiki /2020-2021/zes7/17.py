# 17. Proszę napisać funkcję, która otrzymując jako parametr wskazujący na początek listy
# dwukierunkowej, usuwa z niej wszystkie elementy, w których wartość klucza w zapisie binarnym ma
# nieparzystą ilość jedynek.


from helper_module import arr2dlist, push_front, print_ll, print_back_ll, Node_d
from time import sleep


def no_of_1s_in_biary_odd(num):
    counter = 0

    while num > 0:
        if num % 2 == 1:
            counter += 1
        num //= 2
    
    return counter % 2 == 0


def solve(dl):
    while dl.next != None:
        curr_val = dl.next.val

        if no_of_1s_in_biary_odd(curr_val):
            if dl.next.next != None:
                dl.next.next.prev = dl

            dl.next = dl.next.next
        
        else:
            dl = dl.next
        
    

a = arr2dlist([1, 5,2,35,1,2,3,1,45,1])
# a = arr2list([5,4,7,4353,234,5,5,5,2342,5,77,5])
solve(a)
print_ll(a)
print_back_ll(a)

