from com.abc.banking.account import Account
from queue import Queue # FIFO
from threading import Thread

a = Account('chopras', 'current', 10000)
banking_queue = Queue(maxsize=10) # bound the queue to at the max 10 messages
no_of_withdrawls = 0

# Producer
class WithdrawlInitiationthread(Thread):
    def __init__(self, name, amt):
        super().__init__(name=name)
        self.amt = amt
    def run(self):
        banking_queue.put((self.name, self.amt))

# Consumer
class Withdrawlthread(Thread):
    ''' def __init__(self):
        super().__init__(daemon=True) '''
    def run(self):
        while True:
            item = banking_queue.get()
            # transaction starts
            print('Opening balance as seen by {0} is {1}'.format(item[0], a.acc_balance))
            ub = a.withdraw(item[1])
            print('Updated balance as seen by {0} is {1}'.format(item[0], ub))

            global no_of_withdrawls
            no_of_withdrawls += 1
            # transaction ends

            if no_of_withdrawls == 2:
                break



withdrawlthread = Withdrawlthread()
husband = WithdrawlInitiationthread('Husband', 2000)
wife = WithdrawlInitiationthread('Wife', 5000)

withdrawlthread.start()
husband.start()
wife.start()

