# 23. Dana jest lista, która zakończona jest cyklem. Napisać funkcję, która zwraca liczbę elementów przed
# cyklem.


from helper_module import Node


def find(seen, node):
    for i in range(0, len(seen)):
        if seen[i] == node:
            return i
    
    return -1


def len_cycle(l):
    seen_before = []

    fixer = 0

    if l.val == None: # WARTOWNIK
        seen_before.append(l)
        l = l.next
        fixer = -1


    while l != None:
        ans = find(seen_before, l)
        if ans >= 0:
            if l.val == None: # pętla wskazuje na wartownika
                return 0
            

            return ans + fixer
        

        seen_before.append(l)

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