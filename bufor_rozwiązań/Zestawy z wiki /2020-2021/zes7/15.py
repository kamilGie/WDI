# 15. Proszę napisać funkcję, która otrzymując jako parametr wskazujący na początek listy
# jednokierunkowej, usuwa z niej wszystkie elementy, w których wartość klucza w zapisie trójkowym
# ma większą ilość jedynek niż dwójek.


from helper_module import print_ll, Node, arr2list
from time import sleep

def check(num):
    counter = [0]*3

    while num > 0:
        counter[num % 3] += 1
        num //= 3
    
    return counter[1] > counter[2]


def solve(l):
    while l.next != None:
        curr_val = l.next.val

        if check(curr_val):
            l.next = l.next.next
        else:
            l = l.next  


a = arr2list([2,4,6,1,5,10,4,12])
solve(a)
print_ll(a)