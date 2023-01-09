# List Comprehension is way to create the list from another list or set or dictionary.
import random

# Create the list contain the letter from the string "BHOPAL"

# 1 for loop
my_list = []
for l in "BHOPAL":
    my_list.append(l)
print("List by for loop", my_list)
# 2 lambda fun
my_list = list(map(lambda x: x, "BHOPAL"))
print("List by lambda", my_list)

# 3 using listComprehension
my_list = [x for x in "BHOPAL"]
print("List by list Comprehension", my_list)

nums = [2, 3, 4, 5]
squarelist = []
for i in nums:
    squarelist.append(i ** 2)
print("list by for loop", squarelist)
#
sq_list = list(map(lambda x: x ** 2, nums))
print("list by lambda", sq_list)
#
square_list = [x ** 2 for x in nums]
print("List by list Comprehension ", square_list)

str = "mathmatics"
mlist = [x for x in str if x == 'm']
print(mlist)

names = ['Rahul', 'geeta', 'swati', 'poonam', 'pooja', 'paramjeet', 'yaman', 'pinku']
# create the new list from nameslist if names start with p
pnames = []
for name in names:
    if name.startswith('p'):
        pnames.append(name)
print(pnames)

p_names = [name for name in names if name.startswith('p')]
print(p_names)

# list of number divisible 5
div_list = [x for x in range(1, 100) if x % 5 == 0 and x > 50]
print(div_list)

import numpy

a = numpy.random.randint(10, size=(4, 3))
print(a)
max_ele=[max(i) for i  in a]
print(max_ele)

# Write a program to accept a string from the user, and convert each word of the given string to uppercase ,
# store it in a list and print the list
# str=input('enter the string')
# clist=[x.upper() for x in str.split()]
# print(clist)
# Write a program to accept 5 integers from the user and store them in a list . Now display the list and sum of the elements.
# new_list=[]
# for i in range(5):
#     new_list.append(eval(input('enter the integer:')))
# print('sum of nos in list',sum(new_list))

# or
# text=input('enter the 5 nos:')
# nos_list=[int(x) for x in text.split()]
# print('sum of nos in list',sum(nos_list))

# accept the string remove the vowel from that return the list of remaining.
# str=input('enter the string')
# novowel_list=[x  for x in str if x not in "aeiou"]
# print(novowel_list)

# def get_Number(x):
#     if x in "0123456789":
#         return x
# My_text=input('enter the string:')
# listt=[x for x in My_text if get_Number(x)]
# print(listt)

# Write a program to produce square of only those numbers
# which are divisible by 2 as well as 3 from 1 to 20 , store them in a list and print the list
print("---------------------------")
my_list=[ x**2 for x in range(1,20) if x%2==0 if  x%3==0]
print(my_list)

# Write a function called remove_min_max( ) which accepts a list as argument and removes the
# minimum and maximum elements from the list and returns it
def remove_min_max(my_list):
   my_list=[x  for x in my_list if x!=min(my_list) and x!=max(my_list)]
   return my_list
print("---------------------------")
nos_list=[2,9,8,5,7,11,12]
new_list=remove_min_max(nos_list)
print(new_list)




















































