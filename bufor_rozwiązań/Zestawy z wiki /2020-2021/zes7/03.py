# 3. Proszę napisać funkcję scalającą dwie posortowane listy w jedną
# posortowaną listę. Do funkcji należy przekazać wskazania na pierwsze
# elementy obu list, funkcja powinna zwrócić wskazanie do scalonej listy.
# - funkcja iteracyjna,
# - funkcja rekurencyjna.

# WARTOWNIK


class Node:
    def __init__(self, val = None):
        self.val = val
        self.next = None


def add(l, val):
    if l == None:
        return Node(val)


    while l.next != None:
        l = l.next
    
    l.next = Node(val)



def merge_it(l1, l2):
    l1 = l1.next
    l2 = l2.next

    ans = Node()

    while l1 != None or l2 != None:
        if l1 != None and l2 != None:
            # print(1)
            if l1.val > l2.val:
                # print(11)
                add(ans, l2.val)
                l2 = l2.next
            else:
                # print(12)
                add(ans, l1.val)
                l1 = l1.next
        elif l1 == None:
            # print(2)
            add(ans, l2.val)
            l2 = l2.next
        else:
            # print(3)
            add(ans, l1.val)
            l1 = l1.next
    

    return ans


def merge_rek(l1, l2):
    l1 = l1.next
    l2 = l2.next
    ans = Node()

    def rek(l1, l2, ans):
        if l1 == None and l2 == None:
            return ans

        if l1 != None and l2 != None:
            # print(1)
            if l1.val > l2.val:
                # print(11)
                add(ans, l2.val)
                return rek(l1,l2.next, ans)
            else:
                # print(12)
                add(ans, l1.val)
                return rek(l1.next, l2, ans)
        elif l1 == None:
            # print(2)
            add(ans, l2.val)
            return rek(l1,l2.next, ans)
        else:
            # print(3)
            add(ans, l1.val)
            return rek(l1.next, l2, ans)
    


    return rek(l1, l2, ans)



from helper_module import print_ll

l1 = Node()
add(l1,2)
add(l1,5)
add(l1,44)
add(l1,47)
add(l1,542)
add(l1,54289)
add(l1,54299)

l2 = Node()
add(l2,2)
add(l2,882)
add(l2,54289)


print_ll((l1))
print_ll((l2))

print()

print_ll(merge_rek(l1,l2))
print_ll(merge_it(l1,l2))