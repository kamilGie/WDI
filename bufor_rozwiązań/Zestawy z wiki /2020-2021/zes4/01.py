def print_tab(tab):
    for line in tab:
        print(line)

n = 8

tab = [[0]*n for _ in range(n)]

# tab[1][3] = 4

print_tab(tab)


x, y = 0, 0

x_i, y_i = 1, 1



i = 1
maxi = n**2
while i <= maxi:
    while x < n-1 and tab[y][x+1] == 0:
        tab[y][x] = i
        x += 1
        i += 1
    print(x, y)

    while y < n-1 and tab[y+1][x] == 0:
        tab[y][x] = i
        y += 1
        i += 1
    print(x, y)

    while x > 0 and tab[y][x-1] == 0:
        tab[y][x] = i
        x -= 1
        i += 1
    print(x, y)

    while y > 0 and tab[y-1][x] == 0:
        tab[y][x] = i
        y -= 1
        i += 1
    print(x, y)

    if i == maxi:
        tab[y][x] = i
        i += 1    





# for i in range(1, n*n+1):
#     tab[y][x] = i

#     if x < n-1 and tab[y][x+1] == 0:
#         x += 1
#     elif x == n-x_i and y < n-1 and tab[y+1][x] == 0:
#         y += 1
#     elif y < n-1



print("----------------")
print_tab(tab)
