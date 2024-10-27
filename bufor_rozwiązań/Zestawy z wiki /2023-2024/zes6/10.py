"""
Zadanie 9. Dana jest niepusta lista reprezentująca liczbę naturalną. Kolejne
elementy listy przechowują kolejne cyfry. Proszę napisać funkcję zwiększającą
taką liczbę o 1.

Zadanie 10. Liczby naturalne reprezentowane jak poprzednim zadaniu. Proszę
napisać funkcję dodającą dwie takie liczby. W wyniku dodawania dwóch liczb
powinna powstać nowa lista.
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

# W zadaniu nie jest doprecyzowane, w którym kierunku ułożone są cyfry w
# liście. Najpierw założę, że zaczynamy od najmniej znaczących.
# (czyli 1234 to [4 -> 3 -> 2 -> 1])

def add(a, b):
	head = Node(None) # wartownik
	tail = head
	carry = 0
	while a or b:
		x = a.val if a else 0
		y = b.val if b else 0
		n = x + y + carry
		digit = n  % 10
		carry = n // 10
		tail.next = Node(digit)
		tail = tail.next
		a = a.next if a else None
		b = b.next if b else None
	if carry != 0:
		tail.next = Node(carry)
	return head.next


# A teraz załóżmy że cyfry są przechowywane od najbardziej znaczących.
# 1234 = [1 -> 2 -> 3 -> 4]

# zwraca zawsze liczbę o długości o 1 dłużej niż argumenty, by móc przekazać carry
# np. add2([2], [2]) = [0 -> 4]
# argumenty muszą być tej samej długości!
def add2(a, b):
	if a == b == None: return Node(0)
	assert a != None and b != None
	p     = add2(a.next, b.next)
	n     = a.val + b.val + p.val
	digit = n  % 10
	carry = n // 10
	p.val = digit
	return Node(carry, p)

# wrapper nad add2()
def add3(a, b):
	def linkedlen(p):
		i = 0
		while p:
			i += 1
			p = p.next
		return i

	la = linkedlen(a)
	lb = linkedlen(b)
	while la < lb:
		a = Node(0, a)
		la += 1
	while lb < la:
		b = Node(0, b)
		lb += 1
	# tablice wyrównane do tej samej długości
	c = add2(a, b)
	# pozbywamy się potencjalnego zera na początku
	while c.next and c.val == 0:
		c = c.next
	return c


# pomocnicza - wypisuje ładnie wynik dodawania daną funkcją
def wypisz(a, b, fn):
	# te {} to f-stringi. f"{2+2}" = 4, ale nie musisz tego wiedzieć
	print(f"{fn.__name__}({a}, {b}) = [{fn(a, b)}]")

wypisz(fromarr([7, 3, 1, 2]), fromarr([9, 6]), add)
wypisz(fromarr([2, 1, 3, 7]), fromarr([6, 9]), add3)
print("2137 + 69 =", 2137 + 69)
print()

wypisz(fromarr([9, 9, 9, 9]), fromarr([9, 9, 9]), add)
wypisz(fromarr([9, 9, 9, 9]), fromarr([9, 9, 9]), add3)
print("9999 + 999 =", 9999 + 999)
