from com.abc.college.student import Student
from com.abc.college.professor import Professor

s = Student('mehul', 'm', 10, 90, ['345456564'])
# Student.__init__(4001, 'mehul', 'm', 10, 90, ['345456564'])

p = Professor('jane', 'f', ['Physics'])
# Professor.__init__(4005, 'jane', 'f', ['Physics'])

print(s.name)
print(s.roll)

print(p.name)
print(p.gender)