# A pyhton String is a Sequence of zero or more character .
# String is immutable.
# We can access the element of string But we can not change it.

# Creating the string
# 1 By using the ' '
my_string1='Hello World'
print("String created using the Single quote",my_string1)
# 2 By using the " "
my_string2="Yogesh Pandey"
print("String created using the Double quote",my_string2)
# 3 By using the ''' creating the multiline string '''
my_string3=''' Hello 
              Welcome to Python'''
print("String created using the Triple quote",my_string3)


my_str='Welcome'
print(my_str)

# Accessing the element of string using the While loop
# by while loop
i=0
while i<len(my_str):
    print(my_str[i])
    i+=1
# by for loop
for i in my_str:
    print(i)


city="Bhopal"

# by using the slicing op
print(city[0:4])

# printing the string in reverse order
print(city[::-1])
# using the for loop
for i in range(len(city)-1,-1,-1):
    print(city[i])
























































































