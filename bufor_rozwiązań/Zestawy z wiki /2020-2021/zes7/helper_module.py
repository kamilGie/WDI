
class Node:
    def __init__(self, value = None, next=None):
        self.val = value
        self.next = next
    
    def __str__(self):
        ans = []

        cp = self

        while cp != None:
            ans.append(str(cp.val))
            cp = cp.next
        
        return " -> ".join(ans)


class Node_d:
    def __init__(self, value = None):
        self.val = value
        self.next = None
        self.prev = None



class Node_xy:
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y
        self.next = None



def print_ll(ll: Node):
    c = ll
    if ll.val == None:
        start = ll.next
        print(c.val, end="     ")
        c = c.next
    else:
        start = ll

    if c != None:
        print(c.val, end="     ")
        c = c.next

    while c != None and c != start:
        # if c.val =
        print(c.val, end="     ")
        c = c.next
    print()


def print_back_ll(ll: Node):
    c = ll
    while c.next != None:
        c = c.next

    while c != None:
        print(c.val, end="      ")
        c = c.prev

    print()


def push_back(l: Node, val: int):
    if l == None:
        return Node(val)


    while l.next != None:
        l = l.next
    
    l.next = Node(val)



def arr2list(arr: list):
    """
    Creates Linked List from Python list.
    Returned list has first node empty.
    """

    ans = Node()

    for el in arr:
        push_back(ans, el)
    
    return ans


def arr2dlist(arr: list):
    """
    Creates Doubly Linked List from Python list.
    Returned list has first node empty.
    """


    ans = Node_d()
    c = ans

    for el in arr:
        c.next = Node_d(el)
        c.next.prev = c
        c = c.next    
    
    return ans


def reverse_list(l, ans=None):
    """
    Reverses given list l, glues it to the start of ans and returns ans.
    """

    if l.val == None:
        l = l.next

    if ans == None:
        ans = Node()


    while l != None:
        next_guy = l.next
        l.next = None

        ans_next = ans.next
        ans.next = l
        ans.next.next = ans_next
        
        l = next_guy


    return ans



def push_front(l, val):
    q = Node(val)
    q.next = l.next
    l.next = q



def arr2xylist(arr):
    lis = Node_xy()
    lis_c = lis

    for a, b in arr:
        lis_c.next = Node_xy(a, b)
        lis_c = lis_c.next
    
    return lis


def print_xy(ll):
    while ll != None:
        print("[", end="")
        print(ll.x, ll.y, sep=" | ", end="]\t")

        ll = ll.next
    
    print()



def remove_common(l1, l2):
    """
    Takes pointers to the first elements of two increasing linked lists
    and removes all common elements from both of them
    """
    
    while l1.next != None and l2.next != None:
        if l1.next.val > l2.next.val:
            l2 = l2.next
        elif l1.next.val < l2.next.val:
            l1 = l1.next
        else:
            q = l1.next
            l1.next = l1.next.next
            del q
            
            q = l2.next
            l2.next = l2.next.next
            del q


def remove_common_3l(l1, l2, l3):
    """
    Takes pointers to the 3 increasing linked lists and removes all common elements.
    Returns how many elements was removed from each list.
    """


    counter = 0

    while l1.next != None and l2.next != None and l3.next != None:
        if l1.next.val > l2.next.val:
            l2 = l2.next
        elif l1.next.val < l2.next.val:
            l1 = l1.next
        else:
            val = l1.next.val
            while l3.next != None and l3.next.val < val:
                l3 = l3.next
            
            if l3.next != None and l3.next.val == val:
                q = l1.next
                l1.next = l1.next.next
                del q
    
                q = l2.next
                l2.next = l2.next.next
                del q
    
                q = l3.next
                l3.next = l3.next.next
                del q

                counter += 1
    

    return counter


def make_cycle(ll):
    if ll.next == None:
        raise TypeError("Unable to create cycle from empty list")

    if ll.val == None:
        start = ll.next
    else:
        start = ll
    
    ll = start

    
    while ll.next != None:
        print(ll.next)
        ll = ll.next
    

    
    ll.next = start
    return start


if __name__ == '__main__':
    # print_ll(reverse_list(arr2list([1,44,2,3,4,5]), arr2list([33])))
    # print_ll(make_cycle(arr2list([1,2,3,4,5,6,7])))
    pass