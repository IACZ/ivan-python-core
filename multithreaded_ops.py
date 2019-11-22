# multi threaded way
# Run - 1 process
  # main thread - fibo series
  # user defined thread - copying (IO)

from shutil import copy
from com.abc.lib.series import get_fibo_series
from threading import active_count, current_thread, Thread

# invocation of these functions is context specific
''' print('Active count {0}'.format(active_count()))
print('Current thread {0}'.format(current_thread())) '''

def copying_job(path, destination):
  # user defined thread
  # IO operation (less of CPU)
  copy(path, destination)

  print('Copying done')

path = '/Users/mehul.chopra/Documents/bank.py'
destination = '/Users/mehul.chopra/Desktop'

udt = Thread(target=copying_job, args=(path, destination))
udt.start() # puts the user defined thread in the runnable state (if not running)

# CPU operation

# main thread
n = 30
print(get_fibo_series(n))