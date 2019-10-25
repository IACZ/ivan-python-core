from com.abc.lib.student_ops import get_details, get_grade

name = input('Enter name: ')
roll = int(input('Enter roll: '))
gender = input('Enter gender: ')
marks = float(input('Enter marks: '))

print(get_details(name, roll, gender, marks))
print(get_grade(marks))
