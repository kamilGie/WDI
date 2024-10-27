class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
# end class


def print_all(p):
    while p is not None:
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


# Dwie listy zawierają niepowtarzające się (w obrębie listy) liczby
# naturalne. W obu listach liczby są posortowane rosnąco. Proszę napisać
# funkcję usuwającą z każdej listy liczby nie występujące w drugiej. Do
# funkcji należy przekazać wskazania na obie listy, funkcja powinna zwrócić
# łączną liczbę usuniętych elementów.

def add_guardian_on_back(p):
  first = p
  while p.next is not None:
    p = p.next
  p.next = Node(None)
  return first

def remove(p, q):
  first_p = p
  first_q = q
  p = Node(None,p)
  q = Node(None,q)
  p = add_guardian_on_back(p)
  q = add_guardian_on_back(q)
  counter = 0
  
  while p.next.val is not None and q.next.val is not None:

    if p.next.val == q.next.val:
      p = p.next
      q = q.next
    
    elif p.next.val < q.next.val:
      p.next = p.next.next
      counter += 1
      p = p.next
    elif q.next.val < p.next.val:
      q.next = q.next.next
      counter += 1
      q = q.next
  #end while

  if q.next is not None:
    tail = q
    q = q.next
    while q is not None:
      q = q.next 
      counter += 1
    tail.next = None
  
  if p.next is not None:
    tail = p
    p = p.next
    while p is not None:
      p = p.next
      counter += 1
    tail.next = p 

  return first_p, first_q, counter
  
# end def


T1 = [1, 5, 9, 11, 14, 18, 24, 25]
T2 = [1, 2, 9, 10, 13, 18, 16, 17, 23, 25, 30]

p = create_linked_list(T1)
q = create_linked_list(T2)
p, q, counter = remove(p, q)

print_all(p)
print()
print_all(q)
