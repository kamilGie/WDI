# 19. Elementy w liście są uporządkowane według wartości klucza. Proszę napisać funkcję usuwającą z
# listy elementy o nieunikalnym kluczu. Do funkcji przekazujemy wskazanie na pierwszy element listy,
# funkcja powinna zwrócić liczbę usuniętych elementów.

from helper_module import print_ll, Node, arr2list, push_front, reverse_list
# from time import sleep

def remove_non_uniq(l):
    while l.next != None and l.next.next != None:
        # print("l", l.val, "ln", l.next.val, "lnn", l.next.next.val)
        if l.next.val == l.next.next.val:
            c = l.next.next
            while c != None and c.val == l.next.val:
                c = c.next

            l.next = c
        else:
            l = l.next


a = arr2list([1,1,1,1,3,5,6,7,8,88,88,88,44,222])
remove_non_uniq(a)
print_ll(a)