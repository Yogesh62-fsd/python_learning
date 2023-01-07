# Using slicing operator with list
from typing import List

mynums = [1, 2, 3, 4, 5]
print(mynums[0:4])
print(mynums[0:])
print(mynums[:4])
print(mynums[0:5])
print(mynums[-4:-1])
print(mynums[0:5:2])
# print(mynums[1:4])

# Assigning multiple value to list
# in this element from 1 to 2 i.e start:end-1 are replaced new ones.
# so football and tennis will bed replaced by badminton,rubgy
sports = ['cricket', 'football', 'tennis', 'volleyball', 'hockey']
sports[1:3] = ["badminton", "rubgy"]
print(sports)

# if start end index is same or less then python doesnot replace any thing
# it's simply insert the new element shift rest ones

sports = ['cricket', 'football', 'badminton', 'rubgy', 'volleyball', 'hockey']
sports[1:1] = ["basketball", "handball"]
print(sports)
print("----------------------------------")
sports = ['cricket', 'football', 'tennis', 'volleyball', 'hockey']
print(sports)
# it will remove element from 1 to -3
sports[1:-2] = ['badminton', 'basketball']
print(sports)

# by remove method
print("---------------------------Removing by remove() ------------------------")
sports=['cricket', 'football', 'tennis', 'volleyball', 'hockey']
print(sports)
sports.remove("volleyball")
print(sports)
#  Remove gives error if element is not found.
list1=[2,4,5,6]
# list1.remove(8)
# print(list1)
# If there are multiple copies of same element in list then remove() remove the first occurence of element
print("---------------------------Removing by Multiple copies of same element by remove() ------------------------")
cars=["ciaz","hondacity","ciaz","breza","ciaz"]
print(cars)
cars.remove("ciaz")
print(cars)