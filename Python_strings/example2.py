# Operator in String
import math

state = "Gujurat"
capital = "Ghandhinagar"

# +
print(state + capital)
# *
print(state * 3)
print(state * 0)
print(state * -4)

# in
fruit = 'Banana'
print('nana' in fruit)
print('nani' in fruit)
# not in
print('nana' not in fruit)
print('nani' not in fruit)
# Relation oper

a = 'good'
b = 'morning'
print(a == b)
print(a > b)
print(a >= b)

a = 'Ba' + 'na' * 2
print(a)
# is operator
a = 'London'
b = 'London'
c = 'Paris'
print(a is b)
print(b is c)
print(c is a)

city = 'Rajkot'
# BuiltIN Functions
# len()
print(len(city))
# max () --> Return the max element from the string
print(max(city))
# min() --> Return the min element from the string
print(min(city))
# chr()--> return the character of given integer
print(chr(122))
print(chr(43))
print(chr(1))
# ord()--> return the character take the unicode
print(ord('Y'))
print(ord('a'))

# Strin Interpolation
name = 'Yogesh Pandey'
age = 23
course = 'Btech'
print('Myname is {0} and Age is {1} and course is {2}'.format(name, age, course))
#
# f-string
print(f'My name is{name} and age is {age} and my course is {course}')
# Calling function
a=10
print(f"Number is {a} and factorial is {math.factorial(a)}")