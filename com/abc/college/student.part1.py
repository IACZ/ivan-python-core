# for every class (built in / user defined), an object is created in the memory during program load time
# class object attribute live in the above area of memory

class Student:

  count = 0 # class attribute
  # Access a class attribute
  # Student.count

  def __init__(self, name, gender, roll, marks=None, contact_nos=None): #  None -> variable stores no address
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

    # never == None. Always is None
    if contact_nos is None or not isinstance(contact_nos, list):
      print('Contact nos must be a list')
      self.contact_nos = None
    else:
      self.contact_nos = contact_nos

    Student.count += 1

  # object functions
  def get_details(self):
    # self means the current object
    # s1, s2
    ''' part1 = 'Name: ' + self.name + '\nRoll: ' + str(self.roll) + '\nGender: ' + self.gender \
    + '\nMarks: ' + str(self.marks) + '\n' '''

    ''' part1 = 'Name: {0}\nRoll: {1}\nGender: {2}\nMarks: {3}\n'.format(self.name, self.roll,\
      self.gender, self.marks) '''

    part1 = 'Name: {name}\nRoll: {roll}\nMarks: {marks}\nGender: {gender}\n'.format(\
      marks=self.marks, roll=self.roll, gender=self.gender, name=self.name)

    part2 = 'Contact Nos: \n'
    if self.contact_nos:
      part2 += '\n'.join(self.contact_nos)
      ''' for contact in self.contact_nos:
        part2 += contact + '\n' '''
    else:
      part2 += 'NA'

    return part1 + part2

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

  def get_name_roll(self):
    return (self.name, self.roll)
