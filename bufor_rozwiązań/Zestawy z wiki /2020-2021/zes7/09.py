# 9. Dana jest niepusta lista reprezentująca liczbę naturalną. Kolejne
# elementy listy przechowują kolejne cyfry. Proszę napisać funkcję
# zwiększającą taką liczbę o 1.


from helper_module import reverse_list, Node, push_back, arr2list, print_ll

def add_1(num):
    rev = Node()
    reverse_list(num, rev)

    c = rev.next
    # print(c.val)
    c.val += 1
    next_a = c.val // 10
    c.val %= 10
    c = c.next

    while c != None and next_a != 0:
        c.val += next_a
        next_a = c.val // 10
        c.val %= 10

        c = c.next
    
    if next_a != 0:
        push_back(rev, next_a)


    num = Node()
    reverse_list(rev, num)
    
    return num


print_ll(add_1(arr2list([5,3,7,2,8,9,6])))
print_ll(add_1(arr2list([5,3,7,2,0])))
print_ll(add_1(arr2list([5,0,7,2,4])))
print_ll(add_1(arr2list([5,0,7,8,9])))
print_ll(add_1(arr2list([5,0,7,9,9])))
