# variable no of arguments (0 to n)
def myadd(*args):
  # print(args) # tuple object
  sum = 0
  for arg in args:
    sum += arg
  return sum

# positional arguments packing
print(myadd()) # 0
print(myadd(5)) # 5
print(myadd(5, 5, 4, 6))
print(myadd(5, 6, 7, 3, 5, 6, 7, 8))

def perimeter(length, breadth):
  return 2 * (length + breadth)

stats = (5, 3) # could eveen be a list
# print(perimeter(stats[0], stats[-1]))
# the order of the positional arguments in the function matches with the order of the elements in stats
print(perimeter(*stats))
# positional arguments unpacking


def area(**rect_stats):
  # documentation will be recognized with triple single quotes
  '''
    This accepts keyword arguments `length` and `breadth`
  '''
  # print(rect_stats) # dict object
  return rect_stats['length'] * rect_stats['breadth']

# print(area(4.1, 3.9)) # positional arguments

# keyword arguments packing
print(area(length=4.1, breadth=3.9)) # keywoord arguments
print(area(breadth=3.9, length=4.1))
# print(area(bre=3.9, len=4.1)) # will not work
print(area.__doc__) # prints the documentation of a function


stats_map = {'length': 4.5, 'breadth': 3.2}
# print(perimeter(stats_map['length'], stats_map['breadth']))
# the names of the parameters in the function match with the key names in the dictionary
print(perimeter(**stats_map))

# dictionary unpacking