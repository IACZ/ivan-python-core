# Manager
from com.abc.geometry.square import Square
from com.abc.geometry.rectangle import Rectangle
from com.abc.geometry.circle import Circle

from com.xyz.calc_stats import calc_stats

s = Square(side=5)

''' print(s.area())
print(s.perimeter()) '''

calc_stats(s)

s2 = Square(side=7)
calc_stats(s2)

r1 = Rectangle(length=5, breadth=3)
calc_stats(r1)

c = Circle(radius=4)
calc_stats(c)