# main thread
  # integer n from the end user
  # forking the even nos thread
  # forking the odd nos thread

# user defined thread
  # printing all even nos till n

# user defined thread
  # printing all odd nos till n

from threading import Thread, current_thread

class EvenThread(Thread):
  def __init__(self, n):
    super().__init__(name='Even') # important to do this before doing anything in our constructor
    self.n = n

  def run(self):
    t = current_thread()
    # job
    for i in range(0, self.n + 1, 2):
      print('{0} printing {1}'.format(t.name, i))

class OddThread(Thread):
  def __init__(self, n):
    super().__init__(name='Odd')
    self.n = n

  def run(self):
    # job
    t = current_thread()
    for i in range(1, self.n + 1, 2):
      print('{0} printing {1}'.format(t.name, i))


n = int(input('Enter n: '))

udt1 = EvenThread(n)
udt2 = OddThread(n)

udt1.start()
udt2.start()

# main thread execution should wait on the two user defined threads execution to get over
udt1.join()
udt2.join()

print('Printing all numbers done')

