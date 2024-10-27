# 10. Liczby naturalne reprezentowane jak poprzednim zadaniu. Proszę napisać funkcję dodającą dwie
# takie liczby. W wyniku dodawania dwóch liczb powinna powstać nowa lista.


from helper_module import reverse_list, Node, push_back, arr2list, print_ll

from time import sleep

def add(num1, num2):
    rev1 = Node()
    rev2 = Node()
    reverse_list(num1, rev1)
    reverse_list(num2, rev2)

    ans = Node()


    c1 = rev1.next
    c2 = rev2.next
    # print(c.val)
    next_a = 0
    
    # print_ll(c1)
    # print_ll(c2)

    while c1 != None or c2 != None:
        v = next_a
        if c1 != None:
            v += c1.val
            c1 = c1.next
        if c2 != None:
            v += c2.val
            c2 = c2.next
        
        # print(v, end="\t| ")
        
        next_a = v // 10
        push_back(ans, v%10)

        # print_ll(ans)
        # sleep(0.5)

    # print()
    # print()

    if next_a != 0:
        push_back(ans, next_a)


    num = Node()
    reverse_list(ans, num)
    
    return num




n1 = arr2list([5,3,7,2,8,9,6])
n2 = arr2list([5,8,9,6])

print_ll(add(n1, n2))
