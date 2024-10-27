"""
Zadanie 18. Proszę napisać funkcję, która pozostawia w liście wyłącznie
elementy unikalne. Do funkcji należy przekazać wskazanie na pierwszy element
listy.
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

# zakładam że jeśli element się powtarza to usuwamy wszystkie jego kopie

def dedupe(head):
	if head == None or head.next == None: return head
	p = head
	remove = False
	while p.next:
		if p.next.val == head.val:
			remove = True
			p.next = p.next.next
		else:
			p = p.next
	if remove:
		head = dedupe(head.next)
	else:
		head.next = dedupe(head.next)
	return head

print(dedupe(fromarr([0, 0, 0, 1, 2, 3])))
print(dedupe(fromarr([1, 2, 3, 0, 0, 0])))
print(dedupe(fromarr([0, 0, 1, 2, 3, 0])))
print(dedupe(fromarr([0, 0, 0, 0, 3, 0])))
print(dedupe(fromarr([0, 0, 0, 0, 0, 0])))
print(dedupe(fromarr([1, 2, 3, 1, 2, 4])))
