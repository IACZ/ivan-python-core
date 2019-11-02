from com.abc.college.student import Student

print(Student.count)
s1 = Student('mehul', 'm', 10, 90, ['9878898768', '876787887']) # 4000 -> Student object
# Internally
# 1. 4000 -> Student object
# 2. Student.__init__(4000, 'mehul', 'm', 10, 90)

# s1 = Student()
# Internally
# 1. 4000 -> Student object
# 2. Student.__init__(4000)

name, roll = s1.get_name_roll() # tuple unpacking
# the number of elements in tuple shud be same as the no of variables in which we want to unpack it
# list unpacking

''' name = t[0]
roll = t[1] '''

print(name)
print(roll)
# Student.get_name_roll(s1)


# create attributes in an object
'''s1.name = 'mehul'
s1.gender = 'm'
s1.marks = 67
s1.roll = 10'''


s2 = Student('ivan', 'm', 13, 87, ['4545445645']) # 5003 -> Student object
'''s2.name = 'ivan'
s2.gender = 'm'
s2.marks = 87
s2.roll = 13'''

print(Student.count)

s3 = Student('jane', 'f', 15, 99, '45436546546') # 5005 -> Student object
'''s3.student_name = 'jane'
s3.gen = 'f'
s3.marks = 99
s3.r = 15'''

s3.abc = 'xyz' # object can have its own set of attributes

s4 = Student('jill', 'f', 17)
# Student.__init__(s4, 'jill', 'f', 17)


name = 'mehul chopra' # 5001 -> str object

print(s1.get_details())
# Internally
# Student.get_details(s1)


print(s2.get_details())
# Student.get_details(s2)

print(s1.get_grade())
# Student.get_grade(s1)

print(s2.get_grade())
# Student.get_grade(s2)

print(s3.get_details())
# Student.get_details(s3)

print(s4.get_details())

'''print(type(s1))
print(type(s2))

print(s1)
print(s2)'''

# access attributes from an object
'''print(s1.name)
print(s1.roll)
print(s2.name)
print(s2.roll)'''

print(Student.count)