def abc(): # function object -> abc (module)
  i = 10 # int object -> i (abc)
  j = 20 # int object -> j (abc)
  m = 30 # int object -> m (abc)

  # in python a function can be defined inside another function
  def pqr(): # function object -> pqr (abc)
    print(i) # inner function can access (get) the enclosing function variables (closures)

    j = 40 # int object -> j (pqr)
    print(j) # 40

    # m = m + 40 # does not work
    # print(m)

  pqr()
  print(j) # 20
  print(m) # 30

abc()
# pqr() # this will not work

def mno(x): # function object -> mno (module)
  def rty(y): # function object -> rty (mno)
    return (y ** 2) + x

  # in python a function can return another function
  return rty

m = mno(1) # m -> function object <- rty
n = mno(2) # n -> function object <- rty

print(m(5))
print(n(5))

def fun(x): # function object -> fun (module)
  return x ** 2

def pqr(y, f): # function object -> pqr (module)
  return f(y)

# in python a function can be passed as an argument to another function
ans = pqr(5, fun)
print(ans)