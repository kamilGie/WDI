# 29. Dwie listy zawierają niepowtarzające się (w obrębie listy) liczby naturalne. W obu listach liczby są
# posortowane rosnąco. Proszę napisać funkcję usuwającą z każdej listy liczby nie występujące w
# drugiej. Do funkcji należy przekazać wskazania na obie listy, funkcja powinna zwrócić łączną liczbę
# usuniętych elementów.

from helper_module import print_ll, Node, arr2list


def in_list(lst, val):
    if lst.val == None:
        lst = lst.next
    
    while lst != None and lst.val < val:
        lst = lst.next

    return lst != None and lst.val == val


def remove_sth(l1, l2):
    while l1.next != None:
        if not in_list(l2, l1.next.val):
            l1.next = l1.next.next
        else:
            l1 = l1.next
    

def solve(l1, l2):
    remove_sth(l1, l2)
    remove_sth(l2, l1)


a = arr2list([1,2,3,4,645,7567,42344])
b = arr2list([3,4,5,6,7,8,9])

solve(a, b)
print_ll(a)
print_ll(b)