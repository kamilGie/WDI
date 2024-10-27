class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
#end class


def put_guardian(p):
    q = Node(None)
    q.next = p 
    return q 
#end def


def print_all(p):
    while p is not None:
        print(p.val, end = " ")
        p = p.next
#end def


def create_linked_list(L):
  g = Node(None)
  p = g

  for elem in L:
    p.next = Node(elem)
    p = p.next
  
  return g.next
#end def



# Kolejne elementy listy o zwiększającej się wartości pola val nazywamy
# podlistą rosnącą. Proszę napisać funkcję, która usuwa z listy wejściowej
# najdłuższą podlistę rosnącą. Warunkiem usunięcia jest istnienie w liście
# dokładnie jednej najdłuższej podlisty rosnącej



def find_increasing_sublist(p): # zwraca dlugosc podlisty rosnacej zaczynajacej sie w danym punkcie
    counter = 1

    while p.next is not None and p.next.val > p.val:
        p = p.next
        counter += 1
    #end while

    return counter 
#end def

def remove_longest_increasing_sublist(p):
    p = Node(None,p) # guardian 
    max_cnt        = -1 
    max_cnt_unique = False # zwraca informacje czy jest tylko jedna podlista o takiej najwiekszej dlugosci
    max_cnt_before_start  = None # wskaznik na miejsce przed startem podlisty

    while p.next is not None:
        tmp_cnt = find_increasing_sublist(p.next)
        
        if tmp_cnt > max_cnt:
            max_cnt = tmp_cnt 
            max_cnt_unique = True 
            max_cnt_before_start = p
        
        elif tmp_cnt == max_cnt:
            max_cnt_unique = False 
        
        for _ in range(tmp_cnt): # przechodzimy dalej, bo nie ma sensu szukac podlisty w podliscie, bo bedzie miec na pewno mniejsza dlugosc
                p = p.next 
        # algo 

    #end while

    if max_cnt_unique:

        max_cnt_last = max_cnt_before_start

        for _ in range(max_cnt):
            max_cnt_last = max_cnt_last.next
        
        max_cnt_before_start.next = max_cnt_last.next
         
    else:
        return

#end def

p = create_linked_list( [3,2,4,5,6,7,3] )

remove_longest_increasing_sublist(p)
print_all(p)

