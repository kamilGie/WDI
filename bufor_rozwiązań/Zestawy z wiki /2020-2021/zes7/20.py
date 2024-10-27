# 20. Dana jest lista zawierająca ciąg obustronnie domkniętych przedziałów. Krańce przedziałów
# określa uporządkowana para liczb całkowitych. Proszę napisać stosowne deklaracje oraz funkcję
# redukującą liczbę elementów listy. Na przykład lista: [15,19] [2,5] [7,11] [8,12] [5,6] [13,17] powinien
# zostać zredukowany do listy: [13,19] [2,6] [7,12]

from helper_module import print_ll, arr2list, Node


class Node_pair:
    def __init__(self, a = None, b = None):
        self.a = a
        self.b = b
        self.next = None


def create_summary_list(l):
    ans = Node()

    l_start = l
    while l != None:
        c = ans
        while c.next != None and c.next.val <= l.a:
            c = c.next


        if c.next == None:
            for i in range(l.a, l.b+1):
                c.next = Node(i)
                c = c.next
        else:
            for i in range(l.a, l.b+1):
                if c.next.val <= i:
                    break

                new = Node(i)
                new.next = c.next
                # print("new", end="\t| ")
                # print_ll(new)
                c.next = new

                # print("c2", end = "\t| ")
                # print_ll(c2)

                c = c.next
        # print_ll(ans)

        l = l.next
    
    # print_ll(ans)
    return ans


def print_ll_pair(l):
    while l != None:
        print("(", l.a, " : ", l.b, ")", sep="", end="\t")
        l = l.next
    print()


def shrink(l):
    ans = Node_pair()
    ans_c = ans


    start = l.next.val
    l = l.next


    while l.next != None:
        if l.next.val != l.val + 1:
            ans_c.next = Node_pair(start, l.val)
            start = l.next.val
            
            ans_c = ans_c.next
        
        l = l.next
    

    ans_c.next = Node_pair(start, l.val)

    print_ll_pair(ans)   
    return ans




a = Node_pair(1,4)
a.next = Node_pair(11,16)
a.next.next = Node_pair(7,12)
print_ll_pair(a)

# print("a", end=" ")

# b = Node()
b = create_summary_list(a)
shrink(b)

