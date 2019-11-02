# Module
# name -> menu
'''
1. Fibo series
2. Even series
3. Even or Odd
4. Exit
Please enter ur choice: 1
Enter n: 8
0 1 1 2 3 5 8 13
1. Fibo series
2. Even series
3. Even or Odd
4. Exit
Please enter ur choice: 2
Enter n: 8
0 2 4 6 8
1. Fibo series
2. Even series
3. Even or Odd
4. Exit
Please enter ur choice: 3
Enter n : 9
Odd
1. Fibo series
2. Even series
3. Even or Odd
4. Exit
Please enter ur choice: 4
'''

# Packages
# google -> google.com
# com.google -> com/google/.....

# import the module
# imports only the module; but not the functions from the module
# import series
# import math as m # give a different symbol (name) to the imported module in the current module
import com.abc.lib.math as m # user defined math module

# import the functions directly from the module in the current module
# from series import get_even_series, get_fibo_series as fibo # the module series is never imported in the current module
from com.abc.lib.series import get_even_series, get_fibo_series as fibo

from math import factorial # built in math module

while True:
  # print('1. Fibo series\n2. Even series\n3. Even or Odd\n4. Factorial\n5. Exit')
  print('1. Fibo series', '2. Even series', '3. Even or Odd', '4. Factorial', '5. Exit', sep='\n')
  choice = int(input('Please enter ur choice: ')) # '3' -> 3

  if choice == 5:
    break # forcily breaks out of the enclosing loop

  n = int(input('Enter n: '))
  if choice == 1:
    # fibo series
    # pass # ssignal the python environment to pass this as an empty block and not raise syntax error
    # print(series.get_fibo_series(n))
    # print(get_fibo_series(n))
    print(fibo(n))
  elif choice == 2:
    # even series
    # print(series.get_even_series(n))
    print(get_even_series(n))
  elif choice == 3:
    # even odd
    print(m.evenodd(n))
  else:
    # factorial
    print(factorial(n))