#Write a program to accept 5 unique integers from the user.
# Make sure if the integer being entered is already present in the list your code displays the message
# “Item already present” and ask the user to reenter the integer.

# noslist=[2,5,1,6,9,7,4]
# i=0
# while i<5:
#     n=eval(input('enter the integer:'))
#     if( n in noslist):
#         print('Item alredy present')
#         continue
#     noslist.append(n)
#     i+=1
# print(noslist)

# list1=[]
# for i in range(5):
#     n=eval(input('enter the integer:'))
#     list1.append(n)
# print(list1)
# list2=[]
# for i in range(5):
#     n=eval(input('enter the integer:'))
#     list2.append(n)
# print(list2)
# print("=========================")

# print(list1 in list2)
# Write a program to accept an alphanumeric string from the user.
# Now extract only digits from the given input and add it to the list .
# Finally print the list as well as it’s sum.
# Make sure your list contains numeric representation of digits

list1=[]
s=input('enter the alpha numeric string:')
for s in "0123456789":
    list1.append(s)
print(list1)