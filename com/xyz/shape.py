# enforce my sub classes to follow a protocol (compulsorily override a set of protocol methods)
# 1. Make the current class as abstract
# 2. Mark each of the protocol methods as abstract

# one cannot create an object of an abstract class with abstract methods

from abc import ABC, abstractmethod
class Shape(ABC):

  @abstractmethod
  def area(self):
    pass # abstract

  @abstractmethod
  def perimeter(self):
    pass # abstract

  # non abstract methods