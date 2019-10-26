# for every class (built in / user defined), an object is created in the memory during program load time
# class object attribute live in the above area of memory

class Student:

  count = 0 # class attribute
  # Access a class attribute
  # Student.count

  def __init__(self, name, gender, roll, marks=None): #  None -> variable stores no address
    # create an attribute in an object
    # default arguments must be declared at the end after non default arguments, in the parameter list

    # was called at the time of object creation
    # code that creates attributes in the object (constructs the object)
    # constructor

    # object attribute
    self.name = name
    self.gender = gender
    self.roll = roll
    self.marks = marks

    Student.count += 1

  # object functions
  def get_details(self):
    # self means the current object
    # s1, s2
    return 'Name: ' + self.name + '\nRoll: ' + str(self.roll) + '\nGender: ' + self.gender \
    + '\nMarks: ' + str(self.marks)

  def get_grade(self):
    marks = self.marks
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
