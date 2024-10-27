suma = 10000
best = (2020, 0)

for i in range(2021):
	y = 2020
	x = i
	while x > 0 and y > x:
		x, y = y-x, x
	if x + y < suma:
		suma = x + y
		best = (x, y)

print(suma, best)
