from com.abc.college.book import Book

b1 = Book(title="Book 1", price=900, pages=1000)
b2 = Book(title="Book 2", price=800, pages=500)
b3 = Book(title="Book 3", price=-700, pages=900)

# b1.price = 500
b1.set_price(500)
# Book.set_price(b1, 500)
b1.pages = 900 # pages setter method

b2.pages = 450
b3.price = -500
b3.__price = -500 # doesnt actually modify the private attribute
b3.set_price(-500)

print(b1)
print(b2)
print(b3)

print(b1.get_price())
print(b2.pages) # pages getter method
# Book.get_price(b1)

# protect price - Encapsulation
# 1. prevent outside access of price (private)
# 2. public function (accessed from outside. every function by default is public) which internally
# accesses the private attribute. Public getter/setter method

# Python way of encapsulation
# 1. pages - private attribute of the object
# 2. expose a public property.
  # __pages - pages
# 3. create a getter/setter method the way we did in the above example, but the name of those methods
# must be the property names