# 5. Proszę napisać funkcję, która rozdziela elementy listy odsyłaczowej do
# 10 list, według ostatniej cyfry pola val. W drugim kroku powstałe listy
# należy połączyć w jedną listę odsyłaczową, która jest posortowana
# niemalejąco według ostatniej cyfry pola val.

# WARTOWNIK

class Node:
    def __init__(self, value = None):
        self.val = value
        self.next = None


def push_front(first, val):
    q = Node(val)
    q.next = first.next
    first.next = q
    return first



def push_back(first, val):
    if first is None:
        return val

    p = first
    while p.next is not None:
        p = p.next
    
    p.next = val
    return first


def segment(l):
    t_digits = [0]*10

    for i in range(10):
        t_digits[i] = Node()
    

    l = l.next

    while l != None:
        v = l.val%10
        # print(l.val, v, end=" | ")
        push_front(t_digits[v], l.val)

        l = l.next
    

    return t_digits


def solve(l):
    dig = segment(l)

    ans = Node()

    for i in range(10):
        push_back(ans, dig[i].next)
    

    return ans




from helper_module import arr2list, print_ll

a = arr2list([2,4,6,230,34,6,54234,234,2,34,2,3,4,23,4,234234234457690890,7,56,8,678,23])

print("all", end="\t")
print_ll(a)

result = solve(a)
print_ll(result)