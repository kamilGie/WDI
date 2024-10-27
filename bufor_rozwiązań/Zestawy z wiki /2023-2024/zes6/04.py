"""
Zadanie 4. Proszę napisać funkcję, która dla podanej listy odsyłaczowej odwraca
kolejność jej elementów.
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

# reverse(None) = None
# reverse(x -> None) = x -> None
# reverse(y -> x -> None) = x -> y -> None
# Więc chcemy coś w stylu reverse(x) = reverse(x.next).dodajnakoniec(x)
#
# Do tego celu będę zwracał dwa wskaźniki: do początku listy i na jej koniec.
# Mógłbym niby to otulić w funkcji, która ostatecznie zwracałaby tylko
# początek listy, ale eh.
#
# Zaznaczam, że nie tworzę nowych elementów - nie zużywam żadnej pamięci poza
# stosem.
def reverse(p):
	if p == None: return None, None
	if p.next == None: return p, p

	head, tail = reverse(p.next)
	assert tail and tail.next == None
	tail.next = p
	p.next = None
	return head, tail.next

p = fromarr("garek")
print(p)
print(reverse(p)[0])
