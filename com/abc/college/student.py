# Student IS-A CollegeUser
# Student (child class) CollegeUser (parent class)
# Student (sub class) CollegeUser (super class)
from .college_user import CollegeUser
class Student(CollegeUser):
  def __init__(self, name, gender, roll, marks, contact_nos=None):
    super().__init__(name, gender, contact_nos)
    # CollegeUser.__init__(self, name, gender, contact_nos)

    self.roll = roll
    self.marks = marks