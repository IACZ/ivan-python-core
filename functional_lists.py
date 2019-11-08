pointers = [10, 4, 5, 10, 6, 3, 8, 9, 5, 1]

# get a new list of odd pointers from pointers list (filtering)
# functional programming
# no explicit loops

# higher order function
# encapsulate all the looping, creating a new list, filtering element(lower order function) and adding to new list
''' def filter_list(pointers, fn):
  result = []
  for pointer in pointers:
    if fn(pointer):
      result.append(pointer)

  return result '''

# lower order function
''' def odds(element):
  return element % 2

odd_list = list(filter(odds, pointers))
print(odd_list)'''

odd_list = list(filter(lambda element: element % 2, pointers))
print(odd_list)

# get a new list of even pointers more than 5 from pointers list (filtering)
''' def evens_more_than_5(element):
  return not element % 2 and element > 5
evens = list(filter(evens_more_than_5, pointers))
print(evens) '''

even_list = list(filter(lambda element: not element % 2 and element > 5, pointers))
print(even_list)

# get a new list of pointers deducted by 1 from pointers list (mapping)
''' def deducted_by_one(element):
  return element - 1
dm = list(map(deducted_by_one, pointers))
print(dm) '''

deducted_marks = list(map(lambda element: element - 1, pointers))
print(deducted_marks)