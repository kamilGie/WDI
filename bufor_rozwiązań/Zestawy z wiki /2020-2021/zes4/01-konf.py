size = int(input()) - 1

steps = ((1, 0), (0, 1), (-1, 0) , (0, -1))
x, y = 0, 0
num = 1
arr = [[0]*(size+1) for _ in range(size+1)]

while size > 0:
    for step in steps:
        a, b = step
        for i in range(size):
            arr[y][x] = num
            x, y = x + a, y + b
            num += 1
    size -= 2
    x, y = x + 1, y + 1

if size == 0:
    arr[y][x] = num

for el in arr:
    print(el)




# def spirala(tab,z,n,i):

#     for j in range(i,z):   #w prawo
#         tab[i][j] = n
#         n += 1

#     for l in range(i+1,z):  #w dół
#         tab[l][z-1] = n
#         n += 1

#     for m in range(i+1,z):   #w lewo
#         tab[z-1][-m - 1] = n
#         n += 1

#     for r in range(i+1,z - 1): #w góre
#         tab[-r - 1][i] = n
#         n += 1

#     if 0 in tab[i + 1]:
#         spirala(t, z - 1, n, i + 1)

#     return tab