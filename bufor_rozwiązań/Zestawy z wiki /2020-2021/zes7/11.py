# 11. Lista zawiera niepowtarzające się elementy. Proszę napisać funkcję do której przekazujemy
# wskaźnik na początek oraz wartość klucza. Jeżeli element o takim kluczu występuje w liście należy go
# usunąć z listy. Jeżeli elementu o zadanym kluczu brak w liście należy element o takim kluczu wstawić
# do listy.

# WARTOWNIK

from helper_module import print_ll, arr2list, Node

def remove_or_add(ll, val):
    while ll.next != None:
        if ll.next.val == val:
            ll.next = ll.next.next
            return True
        ll = ll.next


    ll.next = Node(val)
    return False


l = arr2list([2,4,6,7,23,654,234,9])
remove_or_add(l, 65)
print_ll(l)
remove_or_add(l, 6)
print_ll(l)


l = arr2list([])
remove_or_add(l, 65)
print_ll(l)
remove_or_add(l, 6)
print_ll(l)