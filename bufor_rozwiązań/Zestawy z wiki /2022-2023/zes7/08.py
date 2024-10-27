class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
#end class


def put_guardian(p):
    q = Node(None)
    q.next = p 
    return q 
#end def


def print_all(p):
    while p is not None:
        print(p.val, end = " ")
        p = p.next
    #end while
    print()
#end def

def create_link_list(L):
    p = Node( None )
    q = p
    for element in L:
        k = Node( element )
        p.next = k
        p = p.next 
    #end for
    return q.next


# Dana jest niepusta lista, proszę napisać funkcję usuwającą co drugi
# element listy. Do funkcji należy przekazać wskazanie na pierwszy element listy.

def remove_by_two(p):
    q = p
    
    if p is None:
        return None

    while p.next is not None:

        if p.next.next is None:
            p.next = None
            return q

        p.next = p.next.next
        p = p.next
    #end while
    return q

#end def



T1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
T2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]


p = create_link_list(T1)
print_all(p)
p = remove_by_two(p)
print_all(p)

print()

q = create_link_list(T2)
print_all(q)
q = remove_by_two(q)
print_all(q)









