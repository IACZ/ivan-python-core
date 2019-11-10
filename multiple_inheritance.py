# Vendor x
class A:
  def fun(self):
    print('fun of A')

# Vendor y
class B:
  def show(self):
    print('show of B')

  def fun(self):
    print('fun implementation of B')

# company abc
class C(A, B): # MRO (Method resolution order)
  # one child class having more than 1 parent class (super class)
  pass

c = C()
c.show()
c.fun()