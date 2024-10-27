# 25. Dana jest lista, który zakończona jest cyklem. Napisać funkcję, która zwraca wskaźnik do
# ostatniego elementu przed cyklem.


from helper_module import Node


def get_elem_before_cycle(l):
    seen_before = set()

    while True:
        if l.next in seen_before:
            return l
        
        seen_before.add(l)
        l = l.next


a = Node()
a.next = Node(432)
a.next.next = Node(42)
a.next.next.next = Node(555)
# a.next.next.next.next = a.next
a.next.next.next.next = Node(7777)
a.next.next.next.next.next = a.next.next
# a.next.next.next.next = Node(1111115)
# a.next.next.next.next.next = a.next.next

print(get_elem_before_cycle(a).val)

