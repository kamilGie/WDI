"""
Zadanie 13. Proszę napisać funkcję, otrzymującą jako parametr wskaźnik na
pierwszy element listy o wartościach typu int, usuwającą wszystkie elementy,
których wartość jest mniejsza od wartości bezpośrednio poprzedzających je
elementów.
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


#    [2 -> 1 -> 3 -> 7 -> 6 -> 9 -> 1 -> 2 -> 3 -> 3 -> 2 -> 1]
# -> [2 ->      3 -> 7 ->      9 ->      2 -> 3 -> 3]

def zad(p):
	if p == None: return None

	# pierwszy element zawsze jest uwzględniony.
	# odizolujmy go jako początek nowej listy
	tail = p
	p = p.next
	tail.next = None

	# wartość ostatniego elementu jest przechowywana w osobnej zmiennej,
	# na wypadek gdyby został on usunięty
	last = tail.val

	while p:
		next = p.next
		if not (p.val < last):
			tail.next = p
			p.next = None
			tail = p
		last = p.val
		p = next

p = fromarr([2, 1, 3, 7, 6, 9, 1, 2, 3, 3, 2, 1])
print(p)
for _ in range(4):
	zad(p)
	print(p)
