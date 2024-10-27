class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
# end class


def put_guardian(p):
    q = Node(None)
    first = p
    while p.next is not None:
      p = p.next
    p.next = q
    return first 
# end def


def print_all(p):
    while p.next is not None:
        print(p.val, end=" ")
        p = p.next
# end def


def create_linked_list(L):
    g = Node(None)
    p = g

    for elem in L:
        p.next = Node(elem)
        p = p.next

    return g.next
# end def


# Elementy w liście są uporządkowane według wartości klucza. Proszę
# napisać funkcję usuwającą z listy elementy o nieunikalnym kluczu. Do
# funkcji przekazujemy wskazanie na pierwszy element listy,
# funkcja powinna zwrócić liczbę usuniętych elementów


def series(p):
    counter = 0
    p = put_guardian(p)
    first = p
    
    while p.next is not None:
        pointer = p.next

        while pointer.val == p.val:
            pointer = pointer.next
            counter += 1
        p.next = pointer
        p = p.next
        # end while
        
    # end while
    return first, counter
# end def

T = [1,1,2,3,3,3,3,4,5,10,13,14,14,16,19,20,20,20,20,20,20,20,20,20,20,20,20,21]
p = create_linked_list(T)
p, cnt = series(p)
print_all(p)
print()
print(cnt)