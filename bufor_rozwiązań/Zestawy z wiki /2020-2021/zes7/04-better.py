# 4. Proszę napisać funkcję, która dla podanej listy odsyłaczowej odwraca
# kolejność jej elementów.


class Node:
    def __init__(self, val = None):
        self.val = val
        self.next = None



def reverse(l):
    if l == None:
        return None
    if l.next == None:
        return l
    
    p = None
    q = l
    curr = q.next

    while q != None:
        q.next = p
        p = q
        q = curr
        if curr != None:
            curr = curr.next