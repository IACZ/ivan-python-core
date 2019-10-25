def get_details(name, roll, gender, marks):
  return 'Name: ' + name + '\nRoll: ' + str(roll) + '\nGender: ' + gender \
    + '\nMarks: ' + str(marks)

def get_grade(marks):
  '''
    >= 70 - A
    >= 60 - B
    >= 40 - C
    < 40 - F
    > 100 or < 0 - I
  '''
  if marks > 100 or marks < 0:
    grade = 'I'
  elif marks >= 70:
    grade = 'A'
  elif marks >= 60:
    grade = 'B'
  elif marks >= 40:
    grade = 'C'
  else:
    grade = 'F'

  return grade