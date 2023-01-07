#append()
sports = ['cricket', 'football', 'tennis', 'volleyball', 'hockey']
sports.append("rubgy")
print(sports)

nos=[2,4,5,6]
listno=[1,3,9]
listno.append(nos)
print(listno)
#2 extend()
listno=[1,3,9]
# listno.extend(23) TypeErro: int obj is not iterable extend only takes the list.
listno.extend(nos)
print(listno)

car=['breza','ciaz','Hondacity','ertiga']
oldcar=['alto','nano']
car.extend(oldcar)
print(car)

# insert()-->takes 2 argument 1 index (it can negative&positive both)
# 2 argument a element or a list and insert it at given postion
primes=[1,3,5,7]
primes.insert(2,11)
print(primes)
primes.insert(3,[13,17,19,23])
print(primes)
# negative index is also allowed
primes.insert(-2,27)
print(primes)
# index beyond range it do not give error.
primes=[1, 3, 11, 5, 7]
primes.insert(10,[13,3,17])
print(primes)

#index()--->takes the element and return the index of the element if present
# return first occurence or first postion of element if it present more than once.
# if not present then valueerror.

my_list=[1, 3, 11, 5, 7,5,3,5]
print(my_list.index(5))
# x=my_list.index(12)
# print(x) it wil give VAlue Error as 12 is not prsent
vowels=['a','e','i','o','u']
print(vowels.index('i'))

# count()-->return the no of occurence of elementi
#if  element is not present then it gives 0 times
my_list=[1, 3, 11, 5, 7,5,3,5]
print("5 in mylist occurs no of ",my_list.count(5),"times")
# print("15 in mylist occurs no of ",my_list.count(15),"times")

# remove()-->The remove() method searches for the given element in the
# list and removes the first matching element.
# If the element(argument) passed to the remove() method doesn't exist,ValueError exception is thrown.
# remove return none
my_list=[1, 3, 11, 5, 7,5,3,5]
my_list.remove(5)
print(my_list)
# my_list.remove(23) ValueError as 23 is not present.
# print(my_list)

# pop()---->takes the index of element and pop it return it and update the list.
my_list=[1, 3, 11, 5, 7,5,3,5]
x=my_list.pop(2)
print(my_list)
print(x)
# if index is out of range ,then it IndexError: pop index out of range
# y=my_list.pop(12)
# print(my_list)
# print(y)

# if no index is passed by default -1 is passed to it and remove the  last element of the list.
z=my_list.pop()
print(my_list)
print(z)
# index can be negative also.
fruits = ['apple', 'banana', 'cherry']
print(fruits.pop(-3))

# clear()--->clear the list
fruits = ['kiwi','apple', 'gauava','banana', 'cherry','orange']
fruits.clear()
print(fruits)

#  sort ()-->sort the list
# syntax sort(reverse=True/False,key=func())
# fun()--: a function to specify the sorting criteria.
fruits = ['kiwi','apple', 'gauava','banana', 'cherry','orange']
print("Before sorting ",fruits)
fruits.sort()
print("After sorting ",fruits)

# sorting in reverse order
fruits.sort(reverse=True)
print("Sorting in reverse order",fruits)

primes=[19, 13, 11, 5, 29]
primes.sort()
print(primes)
primes.sort(reverse=True)
print(primes)

a = ["january", "february", "march","april"]
a.sort(reverse=True)
print(a)
a.sort(key=len,reverse=True)
print(a)


# reverse()--- reverse the list
my_fruits=['apple', 'banana', 'cherry', 'gauava', 'kiwi', 'orange']
my_fruits.reverse()
print(my_fruits)