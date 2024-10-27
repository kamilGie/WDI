class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
# end class


def put_guardian(p):
    q = Node(None)
    q.next = p
    return q
# end def


def print_all(p):
    while p is not None:
        print(p.val, end=" ")
        p = p.next
# end def


def create_linked_list_with_given_elements(L):
    g = Node(None)
    p = g

    for elem in L:
        p.next = Node(elem)
        p = p.next

    return g.next
# end def


# Dana jestlista, który być może zakończona jest cyklem.
# Napisać funkcję, która sprawdza ten fakt


def cycle(p):

    if p is None:
        return False

    fast = p
    slow = p

    if fast.next != None and fast.next.next != None:
      fast = fast.next.next
      slow = slow.next
    #end if

    while fast.next is not None and fast.next.next is not None:

        if fast == slow:
            return True
        
        fast = fast.next.next
        slow = slow.next
        #end if

    # end while
    return False

# end def


x = Node(1)
p = Node(2)
x.next = p
a = Node(3)
p.next = a
b = Node(4)
a.next = b
c = Node(5)
b.next = c
d = Node(6)
c.next = d

d.next = p

print( cycle(x) ) 
