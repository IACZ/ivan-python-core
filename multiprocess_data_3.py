from multiprocessing import Process, Manager
from com.abc.banking.account import Account
from multiprocessing.managers import BaseManager

class AccountManager(BaseManager):
    pass

AccountManager.register('Account', Account)

with AccountManager() as accntmanager:
    account = accntmanager.Account('mehul', 'Current', 10000)
    print(account.get_acc_name())

    class SimpleProcess(Process):
        def run(self):
            global account

            # Using BaseManager to store custom object in server process memory, one can access
            # only functions on that object. No direct attributes access
            account.set_acc_name('Mehul Chopra')

            print('Account object as seen by squarer process')
            print(account.get_acc_name())

    sp = SimpleProcess()
    sp.start()

    sp.join()

    print('Account object as seen by main process')
    print(account.get_acc_name())

with Manager() as manager:
    numbers = manager.list([3, 4, 2, 1, 6, 7]) # create a list in the server process (manager) memory area

    class SquarerProcess(Process):
        def run(self):
            global numbers

            i = 0
            for n in numbers:
                numbers[i] = n ** 2 # modifying the list in the common memory area shared by manager (server process)
                i += 1
            print('Numbers as seen by squarer process')
            for n in numbers:
                print(n, end=',')
    
    udp = SquarerProcess()
    udp.start()

    # wait for the sqaurer process to get over
    udp.join()

    print('Numbers as seen by main process')
    for n in numbers: # accessing the list from the common memory area shared by manager (server process)
        print(n, end=',')