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

