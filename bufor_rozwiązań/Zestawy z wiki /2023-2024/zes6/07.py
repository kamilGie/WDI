"""
Zadanie 7. Proszę napisać funkcję usuwającą ostatni element listy. Do funkcji
należy przekazać wskazanie na pierwszy element listy.
"""

class Node():
	def __init__(self, val, next=None):
		self.val = val
		self.next = next
	def __str__(self): # własny wymysł do wypisywania listy
		return str(self.val) + (" -> " + str(self.next) if self.next else "")

# pomocnicza - tworzy linked listę z tablicy
def fromarr(arr):
	p = None
	for v in arr[::-1]: # idiom do iterowania przez tablicę wstecz
		p = Node(v, p)
	return p


def removelast(head):
	if head == None or head.next == None: return None
	p = head
	while p.next.next:
		p = p.next
	p.next = None
	return head

p = fromarr([1,2,3,4])
for _ in range(6):
	print(p)
	p = removelast(p)
