# module
# name -> com.abc.lib.series
'''
all library functions that generate any kind of series for the end user
'''

def get_fibo_series(n):
  # '0 1 1 2 3 5 8 13'
  result = ''
  a, b = 0, 1
  result = result + str(a) + '\t' + str(b) + '\t'

  for i in range(1, n-1): # range - end index is exclusive n - 2 + 1
    c = a + b
    result += str(c) + '\t'
    a, b = b, c

  return result


def get_even_series(n):
  # '0 2 4 6 8'
  result = ''
  for i in range(0, n + 1, 2):
    result += str(i) + '\t'
  return result


# print(__name__)
# 1. When the module is run directly = '__main__'
# 2. When the module is not run directly (imported) = 'com.abc.lib.series'

if __name__ == '__main__':
  n = int(input('Enter n: '))
  print(get_fibo_series(n))
  print(get_even_series(n))