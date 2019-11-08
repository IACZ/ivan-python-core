class CollegeUser:
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