# 23. Dana jest lista, która zakończona jest cyklem. Napisać funkcję, która zwraca liczbę elementów w
# cyklu.


from helper_module import Node


def find(seen, node):
    for i in range(0, len(seen)):
        if seen[i] == node:
            return i
    
    return -1


def len_cycle(l):
    seen_before = []

    i = 0
    if l.val == None: # WARTOWNIK
        seen_before.append(l)
        l = l.next
        i += 1

        # seen_before.append()

    while l != None:
        ans = find(seen_before, l)
        if ans >= 0:
            if l.val == None: # NIE WUZGLĘDNIAJ WARTOWNIKA
                return i - ans - 1

            return i - ans
        

        seen_before.append(l)

        i += 1
        l = l.next






a = Node()
a.next = Node(432)
a.next.next = Node(42)
a.next.next.next = Node(555)
# a.next.next.next.next = a.next
# a.next.next.next.next = Node(7777)
# a.next.next.next.next.next = a.next.next
a.next.next.next.next = Node(1111115)
a.next.next.next.next.next = a

print(len_cycle(a))