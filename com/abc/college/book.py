class Book:
  def __init__(self, title, price, pages):
    self.title = title
    self.__price = price # private attribute. Accessible only within the class
    self.pages = pages # pages setter method

  def set_price(self, price):
    if price >= 0:
      self.__price = price
    else:
      print('Price value must be more than or equal to 0')
  
  def get_price(self):
    return self.__price

  # getter
  @property
  def pages(self):
    return self.__pages

  # setter
  @pages.setter
  def pages(self, pages):
    if pages > 0:
      self.__pages = pages
    else:
      raise ValueError('Pages shud be greater than 0')

  def __str__(self):
    return 'Title: {0}\nPrice: {1}\nPages: {2}'.format(\
      self.title, self.__price, self.pages) # pages getter method