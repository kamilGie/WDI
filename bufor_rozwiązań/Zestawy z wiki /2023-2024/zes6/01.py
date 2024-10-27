"""
Zadanie 1. Zaimplementuj zbiór mnogościowy liczb naturalnych korzystając ze
struktury listy odsyłaczowej.
1. czy element należy do zbioru
2. wstawienie elementu do zbioru
3. usunięcie elementu ze zbioru
"""

class Node():
	def __init__(self, val, next=None):
		self.val = val
		self.next = next
	def __str__(self): # własny wymysł do wypisywania listy
		return str(self.val) + (" -> " + str(self.next) if self.next else "")

# Zbiór mnogościowy - (chyba) zwykły zbiór - elementy nie mogą się powtarzać.
# Reprezentuję go jako posortowaną linked listę z wartownikiem.
# Dzięki sortowaniu nie musimy za każdym razem przeszukiwać całej listy.
# Z drugiej strony - działa to tylko dla elementów, które da się porównywać.
def newset(): return Node(None)

def insert(p, val):
	while p.next and p.next.val < val:
		p = p.next
	if p.next and p.next.val == val:
		return # val już jest w zbiorze
	else:
		if p.next: assert val < p.next.val
		p.next = Node(val, p.next)

def contains(p, val):
	while p.next and p.next.val < val:
		p = p.next
	return p.next and p.next.val == val

def remove(p, val):
	while p.next and p.next.val < val:
		p = p.next
	if p.next and p.next.val == val:
		p.next = p.next.next

p = newset()
for v in [2, 1, 3, 7, 4, 2, 0, -69]: insert(p, v)
print(p) # elementy powinny być po kolei i się nie powtarzać

for v in [-69, 0, 1, 2, 3, 4, 7]: assert contains(p, v)
for v in [-100, -10, 5, 6, 8, 9]: assert not contains(p, v)

# usuwamy kilka elementów, w tym niektóre po kilka razy, i niektóre
# których nigdy nie było w zbiorze
for v in [0, 0, 2, 4]: remove(p, v)
print(p)

# sprawdzamy czy faktycznie zostały usunięte
for v in [-69, 1, 3, 7]: assert contains(p, v)
for v in [0, 2, 4]:  assert not contains(p, v)
