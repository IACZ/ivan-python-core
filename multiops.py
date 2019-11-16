# Multiple operations
# 1. Copy a file
# 2. Fibo series

from shutil import copy
from com.abc.lib.series import get_fibo_series

path = '/Users/mehul.chopra/Documents/bank.py'
destination = '/Users/mehul.chopra/Desktop'

# IO operation (less of CPU)
copy(path, destination)

print('Copying done')

# CPU operation
n = 30
print(get_fibo_series(n))

# single threaded way
# Run - 1 process - 1 thread (main thread)
# main thread - step by step

# multi threaded way
# Run - 1 process
  # main thread - fibo series
  # user defined thread - copying (IO)
# Multiple threads try to compete for a CPU for running in a process