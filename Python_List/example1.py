mylist = [1, 2, 3, 4, 5]
print(mylist)
list1 = list(['hello', 2, 4, 3.4])
print(list1)
mystrlist = ['tom', 'jerry', 'spyker']
print(mystrlist)
print(mylist[0])
print(mylist[1])
print(mylist[-4])
print(mylist[-3])

mynums = [10, 20, 30, 40, 50]
mynums[1] = 24
print(mynums)

i = 0
while i < len(mynums):
    print('indexes is ', i, 'elements is', mynums[i])
    i += 1

for i in mynums:
    print(i)
print(len(mynums))
n = len(mynums)
print('List in reverse order:')
for i in range(n - 1, -1, -1):
    print(mynums[i])

# Before append list id is:
print(id(mynums))

# adding new data in list:
mynums.append(60);
print(mynums)
print(id(mynums))
# hence it's prove that the list is mutable when we append new element
# in the list python doesn;t create a new list rather it add element at
# end of list.
