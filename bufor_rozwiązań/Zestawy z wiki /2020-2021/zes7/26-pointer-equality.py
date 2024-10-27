# 26. Proszę napisać funkcję, która sprawdza czy jedna lista zawiera się w drugiej. Do funkcji należy
# przekazać wskazania na pierwsze elementy obu list, funkcja powinna zwrócić wartość logiczną. 


from helper_module import print_ll, Node, arr2list

def chect_if_one_list_is_in_another(start1, start2):
    if start1.val == None:
        start1 = start1.next
    if start2.val == None:
        start2 = start2.next

    l1 = start1
    l2 = start2

    while l1 != None or l2 != None:
        if l1 == start2 or l2 == start1:
            return True
        
        if l1 != None:
            l1 = l1.next
        if l2 != None:
            l2 = l2.next
    
    return False

a = Node(12)
c = a
c.next = Node(11231232)
c = c.next
c.next = Node(222)
c = c.next
c.next = Node(33333)
c = c.next
c.next = Node(20908765)

b = Node(0)
c = b
b = a.next.next

print(chect_if_one_list_is_in_another(a, b))