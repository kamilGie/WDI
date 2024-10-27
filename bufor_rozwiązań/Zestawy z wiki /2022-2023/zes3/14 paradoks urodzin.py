from random import randint

# def prob(N):
#     year = [ - 1 for _ in range(366) ]
#     counter = 0
#
#     for i in range(100):
#         for j in range(N):
#             birthday = randint(0,364)
#             if year[birthday] == i:
#                 counter += 1
#                 break
#             year[birthday] = i
#         #end for 2
#     return counter/100
#
# print( prob(40) )

def SzansaUrodziny(n):
  if (n < 2): return 0
  if (n >= 366): return 1
  szansa = 1
  for i in range(n):
    szansa *= (365 - i) / (365.0)
  return 1 - szansa


def probability_birth( n ):
    dni_roku = [ 0 for i in range(366) ]
    pp = counter = 0

    for _ in range(100):
        for i in range(n):
            birthday = randint(0, 365)
            dni_roku[birthday] += 1
        #end for
        for ele in dni_roku:
            if ele >= 2:
                counter += 1
                break
        #end for
        dni_roku = [ 0 for i in range(366) ]

    return counter / 100




n = int( input() )
print( probability_birth(n) )
print( SzansaUrodziny(n))
