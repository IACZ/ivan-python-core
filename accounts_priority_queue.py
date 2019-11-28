from com.abc.banking.account import Account
from queue import PriorityQueue # FIFO
from threading import Thread
from dataclasses import dataclass, field
from typing import Tuple
from time import sleep

@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Tuple=field(compare=False)

a = Account('chopras', 'current', 10000)
banking_queue = PriorityQueue(maxsize=10) # bound the queue to at the max 10 messages
no_of_withdrawls = 0

# Producer
class WithdrawlInitiationthread(Thread):
    def __init__(self, name, amt, priority):
        super().__init__(name=name)
        self.amt = amt
        self.priority = priority
    def run(self):
        item = PrioritizedItem(priority=self.priority, item=(self.name, self.amt))
        banking_queue.put(item)

# Consumer
class Withdrawlthread(Thread):
    ''' def __init__(self):
        super().__init__(daemon=True) '''
    def run(self):
        while True:
            pitem = banking_queue.get()
            item = pitem.item

            # transaction starts
            print('Opening balance as seen by {0} is {1}'.format(item[0], a.acc_balance))
            ub = a.withdraw(item[1])
            print('Updated balance as seen by {0} is {1}'.format(item[0], ub))

            global no_of_withdrawls
            no_of_withdrawls += 1
            # transaction ends

            if no_of_withdrawls == 2:
                break


husband = WithdrawlInitiationthread('Husband', 2000, 2)
wife = WithdrawlInitiationthread('Wife', 5000, 1)
husband.start()
wife.start()

sleep(5)
withdrawlthread = Withdrawlthread()
withdrawlthread.start()

