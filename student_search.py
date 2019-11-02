from com.abc.college.student import Student

''' slist = [
  Student('mehul', 'm', 10),
  Student('ivan', 'm', 5),
  Student('jane', 'f', 2)
]

roll = int(input('Enter roll to search: '))

for student in slist:
  if student.roll == roll:
    print(student.get_details())
    break
else:
  # will execute whenn the corresponding for loop has been completely exhausted i.e. no break has been encountered
  print('Student not found') '''

smap = {
  10: Student('mehul', 'm', 10),
  5: Student('ivan', 'm', 5),
  2: Student('jane', 'f', 2)
}

roll = int(input('Enter roll to search : '))

if roll in smap:
  student = smap[roll]
  print(student.get_details())
else:
  print('Student not found')