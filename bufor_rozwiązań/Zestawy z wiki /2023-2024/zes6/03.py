"""
Zadanie 3. Proszę napisać funkcję scalającą dwie posortowane listy w jedną
posortowaną listę. Do funkcji należy przekazać wskazania na pierwsze elementy
obu list, funkcja powinna zwrócić wskazanie do scalonej listy.
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

# iteracyjnie
def merge1(a, b):
	head = Node(None) # wartownik
	tail = head
	while a and b:
		assert tail.next == None
		if a.val < b.val:
			tail.next = Node(a.val)
			a = a.next
		else:
			tail.next = Node(b.val)
			b = b.next
		tail = tail.next
	# zostały elementy tylko z jednej z list
	# o ile można niby zrobić `tail.next = a` (lub b), wolę tego nie robić,
	# by późniejsze modyfikacje jednej tablicy nie wpływały na drugą
	if not a: a = b # by nie musieć pisać tej pętli dwa razy
	while a:
		tail.next = Node(a.val)
		tail = tail.next
		a = a.next
	return head.next # pomijamy wartownik

def merge2(a, b):
	if a == b == None: return None
	# jeśli któryś z argumentów ma być pusty, chcę, by to było b
	if a == None: a, b = b, a
	assert a != None

	if b == None:
		# jak ostatnio - mógłbym zwrócić po prostu `a`, ale chcę zrobić kopię
		return Node(a.val, merge2(a.next, b))
	elif a.val < b.val:
		return Node(a.val, merge2(a.next, b))
	else:
		return Node(b.val, merge2(a, b.next))

a = fromarr([-10, -3, 5, 5, 8, 9, 10])
b = fromarr([-20, 0, 9, 9])
print("a =", a)
print("b =", b)

print("\nmerge1:")
print(merge1(a, b))
print(merge1(b, a)) # kolejność powinna być bez znaczenia
print("jeden pusty argument:")
print(merge1(a, None))
print(merge1(None, a))
print("oba puste:")
print(merge1(None, None))

print("\nmerge2:")
print(merge2(a, b))
print(merge2(b, a)) # kolejność powinna być bez znaczenia
print("jeden pusty argument:")
print(merge2(a, None))
print(merge2(None, a))
print("oba puste:")
print(merge2(None, None))
