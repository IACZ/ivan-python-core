from com.abc.banking.account import Account
from threading import Thread, current_thread

a = Account('chopras', 'current', 10000)

# two threads accesssing the joint account
class WithdrawlThread(Thread):
  def __init__(self, account, amt, name):
    super().__init__(name=name)
    self.account = account
    self.amt = amt

  def run(self):
    t = current_thread()
    print('Opening balance as seen by {0} is {1}'.format(t.name, self.account.acc_balance))
    ub = self.account.withdraw(self.amt)
    print('Updated balance as seen by {0} is {1}'.format(t.name, ub))

husband = WithdrawlThread(a, 2000, 'Husband')
wife = WithdrawlThread(a, 5000, 'Wife')

husband.start()
wife.start()