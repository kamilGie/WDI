"""
Zadanie 20. Dana jest lista zawierająca ciąg obustronnie domkniętych
przedziałów. Krańce przedziałów określa uporządkowana para liczb całkowitych.
Proszę napisać stosowne deklaracje oraz funkcję redukującą liczbę elementów
listy. Na przykład lista: [15,19] [2,5] [7,11] [8,12] [5,6] [13,17] powinna
zostać zredukowana do listy: [13,19] [2,6] [7,12]
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

# założenie: przedziały są na ℝ, więc [1;2] ∪ [3;4] != [1;4]

def overlap(a, b, x, y):
	# niech (a, b) zaczyna się przed (x, y)
	if a > x: a, b, x, y = x, y, a, b
	assert a <= x
	return x <= b

def merge(a, b, x, y):
	assert overlap(a, b, x, y)
	return (min(a,x), max(b, y))

def zad(head):
	if head == None or head.next == None: return head
	p = head
	while p.next:
		if overlap(*head.val, *p.next.val):
			# włączamy pierwszy element w ten
			p.next.val = merge(*head.val, *p.next.val)
			head = head.next
			return zad(head)
		p = p.next
	head.next = zad(head.next)
	return head

p = fromarr([(15,19), (2,5), (7,11), (8,12), (5,6), (13,17)])
print(p)
p = zad(p)
print(p)
