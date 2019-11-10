from com.abc.college.student import Student
from com.abc.college.professor import Professor

s = Student('mehul', 'm', 10, 90, ['345456564'])
# Student.__init__(4001, 'mehul', 'm', 10, 90, ['345456564'])

p = Professor('jane', 'f', ['Physics'])
# Professor.__init__(4005, 'jane', 'f', ['Physics'])

i = 10

print(i)
# Internally
# print(i.__str__())
# print(int.__str__(i))

print(s)
# Internally
# print(s.__str__())
# print(Student.__str__(s))

print(p)
# Internally
# print(p.__str__())
# print(Professor.__str__(p))


''' print(s.name)
print(s.roll)

print(p.name)
print(p.gender) '''

# print(s.get_details())
# Student.get_details(s) # calls the overriden method

# print(p.get_details())
# Professor.get_details(p) # calls the inherited method