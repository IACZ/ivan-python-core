# CollegeUser -> object (single inheritance)
class CollegeUser(object): # every class in python implicitly inherits from the object built in class
  # object class signals the Start of inheritance. There is no super class of object class
  def __init__(self, name, gender, contact_nos):
    # self - Student object, Professor object
    # self - any sub class object
    self.name = name
    self.gender = gender
    
     # never == None. Always is None
    if contact_nos is None or not isinstance(contact_nos, list):
      print('Contact nos must be a list')
      self.contact_nos = None
    else:
      self.contact_nos = contact_nos

  def get_details(self):
    # self - Student object, Professor object, sub class object of CollegeUser
    part1 = 'Name: {name}\nGender: {gender}\n'.format(gender=self.gender, name=self.name)
    part2 = 'Contact Nos: \n'
    if self.contact_nos:
      part2 += '\n'.join(self.contact_nos)
    else:
      part2 += 'NA'

    return part1 + part2

  # overriden from the super class object
  def __str__(self):
    return 'Name: {0}\nGender: {1}'.format(self.name, self.gender)
