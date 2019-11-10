# Student IS-A CollegeUser
# Student (child class) CollegeUser (parent class)
# Student (sub class) CollegeUser (super class)
# Student -> CollegeUser -> object (multilevel inheritance)
from .college_user import CollegeUser
class Student(CollegeUser):
  def __init__(self, name, gender, roll, marks, contact_nos=None):
    super().__init__(name, gender, contact_nos)
    # CollegeUser.__init__(self, name, gender, contact_nos)

    self.roll = roll
    self.marks = marks

  # method overrides super class inherited method in its own class
  # signature of the inherited method and the overriden method must be the same
  def get_details(self):
    # self - Student object
    # calling a super class method from sub class, when the inherited method is overriden in the sub class
    part1 = super().get_details()
    # CollegeUser.get_details(self)

    part2 = '\nRoll No: {0}'.format(self.roll)
    return part1 + part2