"""
Zadanie 14. Proszę napisać funkcję, otrzymującą jako parametr wskaźnik na pierwszy element listy o
wartościach typu int, usuwającą wszystkie elementy, których wartość dzieli bez reszty wartość bezpośrednio
następujących po nich elementów.
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
	for v in arr[::-1]: p = Node(v, p)
	return p


def zad(p):
	if p == None: return None

	# można przyjąć że dzielenie przez zero nie ma reszty
	while p.next and (p.val == 0 or p.next.val % p.val == 0):
		p = p.next
	p.next = zad(p.next)
	return p

p = fromarr([2, 4, 8, 9, 3, 3, 3, 9, 2, 0, 4, 8])
print(p)
p = zad(p)
print(p)
