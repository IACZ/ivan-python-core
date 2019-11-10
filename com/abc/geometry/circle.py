from math import pi
from com.xyz.shape import Shape

class Circle(Shape):
  def __init__(self, radius):
    self.radius = radius

  def area(self):
    return pi * (self.radius ** 2)

  def perimeter(self):
    return 2 * pi * self.radius