# 4. Proszę napisać funkcję, która dla podanej listy odsyłaczowej odwraca
# kolejność jej elementów.



class Node:
    def __init__(self, val = None):
        self.val = val
        self.next = None


def push_back(l, val):
    if l == None:
        return Node(val)


    while l.next != None:
        l = l.next
    
    l.next = Node(val)



def reverse(l, ans):
    if l.next != None:
        reverse(l.next, ans)
    
    if l.val != None:
        push_back(ans, l.val)



from helper_module import print_ll

test = Node()
push_back(test, 52)
push_back(test, 57)
push_back(test, 576)
push_back(test, 74)
push_back(test, 1)
push_back(test, 15345345)
push_back(test, 153)

ans = Node()
reverse(test, ans)
print_ll(ans)