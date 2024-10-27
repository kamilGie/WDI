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
#end def


def create_linked_list(L):
  g = Node(None)
  p = g

  for elem in L:
    p.next = Node(elem)
    p = p.next
  
  return g.next
#end def




# Proszę napisać funkcję scalającą dwie posortowane listy w jedną
# posortowaną listę. Do funkcji należy przekazać wskazania na pierwsze
# elementy obu list, funkcja powinna zwrócić wskazanie do scalonej listy.
# - funkcja iteracyjna,
# - funkcja rekurencyjna.


# To jest zadanie 3



def merge_iteracyjne(p,q):
    k = Node( None )
    first = k

    if q is None: return p
    if p is None: return q

    while p is not None and q is not None:

        if p.val > q.val:
            k.next = q
            q = q.next
            k = k.next

        elif p.val < q.val:
            k.next = p
            p = p.next
            k = k.next

        else: # p.val == q.val

            k.next = p
            p = p.next
            k = k.next

            k.next = q
            q = q.next
            k = k.next
    #end while

    if p is None and q is not None:
        k.next = q
    else:
        k.next = p
    #end if

    return first
#end def



T1 = [1,2,14,39,40,41,78,93]
T2 = [3,7,9,15,40,83,92]


p = create_linked_list( T1 )
q = create_linked_list( T2 )
k = merge_iteracyjne(p,q)
print_all(k.next)


