# ====================================================================================================>
# Zadanie 2B, 2024-01-04
# Na liczbach naturalnych możemy wykonywać następujące operacje:
# 1. 𝐴(𝑛) zamienia liczbę 𝑛 na sumę jej podzielników właściwych (mniejszych od samej liczby), np.
# 𝐴(1) = 1, 𝐴(6) = 6, 𝐴(12) = 16, 𝐴(17) = 1.
# 2. 𝐵(𝑛) zamienia liczbę 𝑛 na najmniejszy, większy od tej liczby wyraz ciągu Fibonacciego, np.
# 𝐵(1) = 2, 𝐵(4) = 5, 𝐵(8) = 13.
# 3. 𝐶(𝑛) zwiększa liczbę 𝑛 o liczbę będącą rewersem liczby 𝑛, np. 𝐶(1) = 2, 𝐶(10) = 11, 𝐶(13) = 44
# Proszę napisać funkcję cycle(x,n), która sprawdza czy startując od liczby 𝑥 możemy do niej powrócić
# wykonując sekwencję operacji spośród A,B,C o długości większej od 1 i nie większej od n. Jeżeli jest to
# możliwe, funkcja powinna zwrócić długość znalezionej sekwencji operacji, w przeciwnym wypadku
# należy zwrócić wartość 0.
# Na przykład wywołanie:
# cycle(29,6) powinno zwrócić 4 (cykl 29, B, 55, B, 89, C, 187, A, 29), [przykład jest błędny, 𝐵(29) = 34]
# cycle(31,6) powinno zwrócić 0.
# ====================================================================================================>

# przepisane z wykładu 2024-01-08
# używa appenda do wizualizacji

end=None

def A(n):
  s = 1
  p = 2
  while p*p<n:
    if n%p==0: s += p+n//p
    p += 1
  end
  if p*p == n: s += p
  return s
end

def B(n):
  a,b = 1,1
  while a<=n:
    a,b = b,a+b
  end
  return a
end

def C(n):
  n2 = n
  r = 0
  while n>0:
    r = 10*r+n%10
    n//=10
  end
  return r+n2
end

def rek(a,b,n,l,res=[]):
#  print(a,end=' ')
  if a==b:
    print(res+[b])
    return l

  if n==0: return None
  if r := rek(A(a),b,n-1,l+1,res+[a,"A"]): return r
  if r := rek(B(a),b,n-1,l+1,res+[a,"B"]): return r
  if r := rek(C(a),b,n-1,l+1,res+[a,"C"]): return r
  return None

def cycle(a,n):
  if r := rek(A(a),a,n-1,1,res=["A"]): return r
  if r := rek(B(a),a,n-1,1,res=["B"]): return r
  if r := rek(C(a),a,n-1,1,res=["C"]): return r

  return -1
end




while True:
  a = int(input('>>'))
  print(cycle(a,10))

