"""
Zadanie 8. Dana jest niepusta lista, proszę napisać funkcję usuwającą co drugi
element listy. Do funkcji należy przekazać wskazanie na pierwszy element listy.
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

# Usuwam co drugi element, nie wliczając pierwszego.
def removeeven(p):
	if p == None: return None
	while p:
		if p.next:
			p.next = p.next.next
		p = p.next

p = fromarr([0,1,2,3,4,5,6,7,8,9,10])
print(p)
for _ in range(5):
	removeeven(p)
	print(p)
