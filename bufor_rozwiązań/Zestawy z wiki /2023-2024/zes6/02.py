"""
Zadanie 2. Zastosowanie listy odsyłaczowej do implementacji tablicy rzadkiej.
Proszę napisać trzy funkcje:
– inicjalizującą tablicę
– zwracającą wartość elementu o indeksie n
– podstawiającą wartość value pod indeks n
"""

class Node():
	def __init__(self, val, next=None):
		self.val = val
		self.next = next
	def __str__(self): # własny wymysł do wypisywania listy
		return str(self.val) + (" -> " + str(self.next) if self.next else "")

# Podobnie jak w ostatnim zadaniu, tablicę rzadką przechowam jako linked listę
# z wartownikiem par (indeks, val), posortowaną według indeksu. Żaden indeks
# nie może się pojawić dwa razy.
def newset(): return Node(None)

# p - wskaźnik do wartownika
# k - indeks (od angielskiego key)
# v - wartość
def set(p, k, v):
	# W teorii pary możemy porównywać bezpośrednio, (a, b) < (c, d)
	# W tym zadaniu nawet to zadziała, ale ogólnie rzecz biorąc program się
	# wysypie jeśli a == c, a `b` i `d` będą nieporównywalne.
	while p.next and p.next.val[0] < k:
		p = p.next

	# wstawanie gdzieś None traktuję jako usuwanie elementu
	if v == None:
		if p.next and p.next.val[0] == k:
			p.next = p.next.next
	else:
		if p.next and p.next.val[0] == k:
			# indeks już w liście - nadpisujemy go
			p.next.val = (k, v)
		else:
			p.next = Node((k, v), p.next)

def get(p, k):
	while p.next and p.next.val[0] < k:
		p = p.next
	return p.next.val[1] if p.next.val[0] == k else None

p = newset()
set(p, 1, 1)
set(p, 10, 2)
set(p, 1, 3)
set(p, 2, 4)
set(p, 2, None)
set(p, 4, None)
print(p) # None -> (1, 3) -> (10, 2)

assert get(p, 1) == 3
assert get(p, 2) == None
assert get(p, 3) == None
assert get(p, 10) == 2
