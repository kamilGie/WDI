from math import sqrt


def prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0 or n <= 1:
        return False
    i = 5
    while i <= sqrt(n) + 1:
        if n % i == 0:
            return False
        i += 2
        if n % i == 0:
            return False
        i += 4
    # end while
    return True


def zad5(T):
  def rek(T, i, x, k):
    x *= 2
    x += T[i]

    if i - k + 1 > 30:
      return False

    if i == len(T)-1:
      if prime(x):
        return True
      return False

    if prime(x):
      return rek(T, i+1, 0, i+1) or rek(T, i+1, x, k)
    return rek(T, i+1, x, k)

  return rek(T, 0, 0, 0)


print( zad5([1, 1, 0, 1, 0, 0]) )
print( zad5([1,1,1,0,1,1]) )