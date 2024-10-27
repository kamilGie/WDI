"""
Zadanie 21. Kolejne elementy listy o zwiększającej się wartości pola val
nazywamy podlistą rosnącą. Proszę napisać funkcję, która usuwa z listy
wejściowej najdłuższą podlistę rosnącą. Warunkiem usunięcia jest istnienie w
liście dokładnie jednej najdłuższej podlisty rosnącej.
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
	bestlen = 0
	start, end = None, None

	# zakładam, że lista nie zaczyna się wartownikiem - więc zrobię własny
	p = Node(None, p)
	head = p

	while p and p.next:
		assert p.val == None or not (p.val < p.next.val)
		# następna podlista zaczyna się od następnego elementu
		# dzięki zaczynaniu iteracji o 1 wstecz, łatwiej mi ją potem usunąć

		before = p
		p = p.next

		cur = 1
		while p.next and p.val < p.next.val:
			cur += 1
			p = p.next
		# w tym momencie albo nie ma p.next,
		# albo p.next nie jest częścią podlisty

		if cur == bestlen:
			# druga podlista o tej samej długości - pozbędę się wskaźników
			# do pierwszej, by jej potem nie usunąć
			start, end = None, None
		elif cur > bestlen:
			bestlen = cur
			start, end = before, p.next

	if start:
		start.next = end

	return head.next # pozbywamy się wartownika


def wypisz(a):
	print(f"zad({a}) = {zad(a)}")
wypisz(fromarr([1,2,3,1,2,3]))
wypisz(fromarr([1,2,3]))
wypisz(fromarr([1,2,3,1,2]))
wypisz(fromarr([1,2,1,2,3]))
wypisz(fromarr([1,1,1,1,1]))
wypisz(fromarr([1,1,2,3,1]))
