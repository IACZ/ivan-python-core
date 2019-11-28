from com.abc.banking.account import Account
from threading import Thread, current_thread, Lock

a = Account('chopras', 'current', 10000)
lock = Lock() # 1 lock per account

# two threads accesssing the joint account
class WithdrawlThread(Thread):
  def __init__(self, account, amt, name):
    super().__init__(name=name)
    self.account = account
    self.amt = amt

  def run(self):
    t = current_thread()

    result = lock.acquire(timeout=15)
    if not result:
      print('Transaction timeout error. Please try again later')
      return

    try:
      # transaction starts
      print('Opening balance as seen by {0} is {1}'.format(t.name, self.account.acc_balance))
      ub = self.account.withdraw(self.amt)
      print('Updated balance as seen by {0} is {1}'.format(t.name, ub))
      # transaction ends
    finally:
      lock.release()

husband = WithdrawlThread(a, 2000, 'Husband')
wife = WithdrawlThread(a, 5000, 'Wife')

husband.start()
wife.start()

# synchronized access to the common data that the threads operate on
# Locks
# 1 Lock per common data
# Just before modifying anything in the common data, acquire the lock
# Once modification done on that common data, release the lock
# Multiple threads compete for that 1 lock