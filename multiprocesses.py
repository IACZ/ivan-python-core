from multiprocessing import cpu_count, Process
from shutil import copy
from com.abc.lib.series import get_fibo_series

# print(cpu_count())

def copying_job(path, destination):
  # user defined thread
  # IO operation (less of CPU)
  copy(path, destination)

  print('Copying done')

path = '/Users/mehulchopra/Documents/personal/training/ivan-python-core/math_ops.py'
destination = '/Users/mehulchopra/Desktop'

if __name__=='__main__':
  udp = Process(target=copying_job, args=(path, destination))
  udp.start()

  # CPU operation
  n = 1000
  print(get_fibo_series(n))

  udp.join() # ensures that the subprocess is destroyed once its work is done and is not lingering
