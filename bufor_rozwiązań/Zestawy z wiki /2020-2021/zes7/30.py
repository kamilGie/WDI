# 30. Dane są dwie niepuste listy, z których każda zawiera niepowtarzające się elementy. Elementy w
# pierwszej liście są uporządkowane rosnąco, w drugiej elementy występują w przypadkowej
# kolejności. Proszę napisać funkcję, która z dwóch takich list stworzy jedną, w której uporządkowane
# elementy będą stanowić sumę mnogościową elementów z list wejściowych.
# Do funkcji należy przekazać wskazania na obie listy, funkcja powinna zwrócić wskazanie na listę
# wynikową. Na przykład dla list:
# 2 -> 3 -> 5 ->7-> 11
# 8 -> 2 -> 7 -> 4
# powinna pozostać lista:
# 2 -> 3 -> 4 -> 5 ->7-> 8 -> 11

from helper_module import print_ll, Node, arr2list


def insert(lst, val):    
    while lst.next != None and lst.next.val < val:
        lst = lst.next

    if lst.next == None:
        lst.next = Node(val)
        return

    if lst.next.val == val:
        return
    
    q = Node(val)
    q.next = lst.next
    lst.next = q

def union(ordered, not_ordered):
    if not_ordered.val == None:
        not_ordered = not_ordered.next
    
    while not_ordered != None:
        insert(ordered, not_ordered.val)
        not_ordered = not_ordered.next

    return ordered


a = arr2list([2,4,5,6,7,876])
b = arr2list([63,234,25,6,1,2,4])

print_ll(union(a,b))