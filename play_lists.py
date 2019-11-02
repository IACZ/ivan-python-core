pointers = [10, 1, 10, 3, 6, 7, 8, 5, 3, 2]

# get a new list of evens elements from pointers list (filtering)
''' evens = []
for pointer in pointers:
  if not pointer % 2:
    evens.append(pointer)

print(evens) '''

# for comprehensions
# Pre requisite  : get a new list
evens = [pointer for pointer in pointers if not pointer % 2]
print(evens)

# get a new list of odd elemens greater than or equal to 5 from pointers list (filtering)
odds = [pointer for pointer in pointers if pointer % 2 and pointer >= 5]
print(odds)

# get a new list of pointers deducted by 1 from pointers list (mapping)
deducted_marks = [pointer - 1 for pointer in pointers]
print(deducted_marks)

# get a new list of squares of pointers that are oddd and >=5 from pointers list (filtering + mapping)
ans = [pointer ** 2 for pointer in pointers if pointer % 2 and pointer >= 5]
print(ans)