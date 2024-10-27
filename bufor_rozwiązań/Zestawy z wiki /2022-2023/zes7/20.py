class Node:
    def __init__(self, _start=-float('inf'), _end=float('inf'), next=None):
        self.start = _start
        self.end = _end
        self.next = next
# end class


def put_guardian(p):
    q = Node(None)
    q.next = p
    return q
# end def


def print_all(p):
    while p is not None:
        print('[' + str(p.start) + ',' + str(p.end) + ']', end=" ")
        p = p.next
# end def


def create_linked_list(L):
    g = Node(None)
    p = g

    for elem in L:
        p.next = Node(elem[0], elem[1])
        p = p.next

    return g.next
# end def


#  Dana jest lista zawierająca ciąg obustronnie domkniętych przedziałów.
# Krańce przedziałów określa uporządkowana para liczb całkowitych. Proszę
# napisać stosowne deklaracje oraz funkcję redukującą liczbę elementów listy.
# Na przykład lista: [15,19] [2,5] [7,11] [8,12] [5,6] [13,17]
# powinien zostać zredukowany do listy: [13,19] [2,6] [7,12]


def intersect(p, q):
  return ( p.start >= q.start and p.start <= q.end ) or ( p.end > q.start and p.end <= q.end )


def common_section(p,q):
  return min(p.start,q.start), max(p.end, q.end)


def merge(p):
  if p is None:
      return None

  p.next = merge(p.next)

  tmp = p
  while tmp.next is not None:
    if intersect(p, tmp.next):
      _start, _end = common_section(p, tmp.next)
      p.start = _start 
      p.end = _end 
      tmp.next = tmp.next.next 
    else:
      tmp = tmp.next 
  #end while

  return p
#end def 

p = create_linked_list( [ [15,19], [2,5], [7,11], [8,12], [5,6], [13,17] ] )
print_all(p)
print()
p = merge(p)
print_all(p)