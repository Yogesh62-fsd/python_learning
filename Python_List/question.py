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

list1=[]
for i in range(5):
    n=eval(input('enter the integer:'))
    list1.append(n)
print(list1)
list2=[]
for i in range(5):
    n=eval(input('enter the integer:'))
    list2.append(n)
print(list2)
print("=========================")

print(list1 in list2)