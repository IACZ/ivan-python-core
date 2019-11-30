from time import sleep

class Account:
  def __init__(self, acc_name, acc_type, acc_balance):
    self.acc_name = acc_name
    self.acc_type = acc_type
    self.acc_balance = acc_balance

  def withdraw(self, amt):
    self.acc_balance -= amt
    # sleep(4) # some more time for the execution of this method
    return self.acc_balance

  def __str__(self):
    return 'Name: {0}\nType: {1}\nBal: {2}'.format(self.acc_name, self.acc_type, self.acc_balance)

  def get_acc_name(self):
    return self.acc_name

  def set_acc_name(self, name):
    self.acc_name = name