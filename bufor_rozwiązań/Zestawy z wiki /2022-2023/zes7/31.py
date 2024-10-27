# Proszę napisać funkcję, która rozdziela listę na dwie listy. Pierwsza
# powinna zawierać klucze parzyste dodatnie, drugi klucze nieparzyste ujemne,
# pozostałe elementy należy usunąć z pamięci. Do funkcji należy przekazać
# wskaźniki na listę z danymi oraz wskaźniki na listy wynikowe. Funkcja
# powinna zwrócić liczbę usuniętych elementów


class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
#end class


def put_guardian(p): # tworzy guardiana 
    g = Node( None, p )
    return g 
#end def 


def add(p, new_val): # dodawanie rekurencyjne

    if p.next is None:
        q = Node(new_val)
        p.next = q
        return

    if p.next is not None:
        if p.next.val == new_val:
            return

        elif p.next.val > new_val:
            q = Node(new_val)
            q.next = p.next 
            p.next = q
        else:
            add(p.next, new_val)
    #end if 
#end def


def print_all(p):
    while p is not None:
        print(p.val, end = " ")
        p = p.next
    #end while
    print()
#end def


def create_linked_list_with_given_elements(L):
  g = Node(None)
  p = g

  for elem in L:
    p.next = Node(elem)
    p = p.next
  
  return g.next
#end def



def separation(p,a,b):
    p = put_guardian( p )
    cnt = 0
    q = p

    while p.next is not None:

        if p.next.val % 2 == 0 and p.next.val > 0:
            tmp = p.next
            p.next = p.next.next

            # Doklejanie elementu do link listy a na poczatek:
            tmp.next = a.next 
            a.next = tmp 
        
        elif p.next.val % 2 == 1 and p.next.val < 0:
            tmp = p.next
            p.next = p.next.next

            # Doklejanie elementu do link listy b na poczatek:
            tmp.next = b.next 
            b.next = tmp 
        
        else:
            p.next = p.next.next
            cnt += 1 
    #end while
    return cnt,a,b
    # daj jeszcze returna na pozostale listy, sprawdz program
#end def

a = None
a = put_guardian(a)
b = None
b = put_guardian(b)

T = [1,-2,-3,4,-5,6,7,-8,9,10,11,12]

p = create_linked_list_with_given_elements( T )


cnt,a,b= separation(p,a,b)
print_all(a.next)
print_all(b.next)
print(cnt)







