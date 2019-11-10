from .shape import Shape

# Vendor of xyz company
def calc_stats(shape):
  # shape passed to this function must be a sub class of Shape class
  if isinstance(shape, Shape):
    # this will even return true when shape is an object whose class inherits from Shape
    print('Area: {0}'.format(shape.area()))
    print('Perimeter: {0}'.format(shape.perimeter()))
  else:
    print('Error. Did u inherit from Shape class')