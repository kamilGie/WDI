# 3. Proszę napisać funkcję scalającą dwie posortowane listy w jedną
# posortowaną listę. Do funkcji należy przekazać wskazania na pierwsze
# elementy obu list, funkcja powinna zwrócić wskazanie do scalonej listy.
# - funkcja iteracyjna,
# - funkcja rekurencyjna.


class Node:
    def __init__(self, value = None):
        self.val = value
        self.next = None

def merge_it(l1, l2):
    # WARTOWNIK

    ans = Node()
    c_ans = ans

    if l1.val == None:
        l1 = l1.next
    if l2.val == None:
        l2 = l2.next


    while l1 != None and l2 != None:
        if l1.val < l2.val:
            c_ans.next = l1
            l1 = l1.next
            c_ans = c_ans.next
        else:
            c_ans.next = l2
            l2 = l2.next
            c_ans = c_ans.next
    
    
    if l1 != None:
        c_ans.next = l1
    if l2 != None:
        c_ans.next = l2
    
    return ans.next


def merge_rek(l1, l2):
    if l1 == None:
        return l2
    if l2 == None:
        return l1
    
    if l1.val < l2.val:
        res = l1
        res.next = merge_rek(l1.next, l2)
    else:
        res = l2
        res.next = merge_rek(l1, l2.next)
    
    return res



# from helper_module import arr2list, print_ll

# a = arr2list([1,2,3,4,7,8,99])
# b = arr2list([3,4,55,666,4323,23455])

# print_ll(merge_it(a, b))