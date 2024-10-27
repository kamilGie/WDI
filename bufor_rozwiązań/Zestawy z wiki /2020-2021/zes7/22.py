# 22. Dana jest lista, który być może zakończona jest cyklem. Napisać funkcję, która sprawdza ten fakt.


from helper_module import Node, arr2list


def is_cycle(l):
    seen_before = set()

    while l != None:
        if l in seen_before:
            return True
        
        seen_before.add(l)
        l = l.next
    
    return False


a = arr2list([3,234,23,42,5,2,432,35,34,53,324])
print(is_cycle(a))

print()

a = Node()
a.next = Node(432)
a.next.next = Node(42)
a.next.next.next = Node(555)
a.next.next.next.next = a
print(is_cycle(a))
