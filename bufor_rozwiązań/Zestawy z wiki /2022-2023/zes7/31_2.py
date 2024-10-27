# 31. Proszę napisać funkcję, która rozdziela listę na dwie listy. Pierwsza
# powinna zawierać klucze parzyste dodatnie, drugi klucze nieparzyste ujemne,
# pozostałe elementy należy usunąć z pamięci. Do funkcji należy przekazać
# wskaźniki na listę z danymi oraz wskaźniki na listy wynikowe. Funkcja
# powinna zwrócić liczbę usuniętych elementów. 

class Node:
  def __init__(self, val, next = None):
    self.val = val
    self.next = next

def print_all(p):
  if p is not None:
    print(p.val)
    print_all(p.next)

def create_from_list(L):
  g = Node(None)
  p = g

  for elem in L:
    p.next = Node(elem)
    p = p.next
  
  return g.next
#q = Node(1)
# Node(none)  -> Node(2) -> Node(3) -> None

# p - lista ktora chcemy rozdzielic, nie ma wartownika
# a - lista z parzystymi dodatnimi
# b - lista ta druga
def rozdziel(p, a, b):
  cnt = 0
  # dorabiamy wartownik

  p = Node(None, p)

  while p.next != None:
    q = p.next

    p.next = p.next.next

    if q.val % 2 == 0 and q.val > 0:
      q.next = a.next
      a.next = q
    elif q.val % 2 == 1 and q.val < 0:
      q.next = b.next
      b.next = q
    else:
      cnt += 1
    
  return cnt

p = create_from_list([7, 8, 6, -1, -2, 4, -3, 0])
a = Node(None)
b = Node(None)

rozdziel(p, a, b)



print_all(b)