# Developer X

# Square IS-A Shape
from com.xyz.shape import Shape

class Square(Shape):
  def __init__(self, side):
    self.side = side

  def area(self):
    return self.side ** 2

  def perimeter(self):
    return 4 * self.side