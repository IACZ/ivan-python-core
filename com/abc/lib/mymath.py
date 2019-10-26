from math import factorial as fact, sqrt as sq

class MyMath:

  # class functions
  # accessed using ClassName.functioncall()
  # class functions do not have a self
  def factorial(n):
    return fact(n)

  def sqrt(n):
    return sq(n)