# 1 len()
list1=[2,5,3,7,8,9]
print('Lenght of list is ',len(list1))
# max()
print("Maximum element in list",max(list1))
# min()
print("Minimum element in list",min(list1))
# sum()
print("sum of all element of list",sum(list1))
# sorted()
print("Sorted element of list are",sorted(list1))
#  To sort in reverse order
print("sorted element in reverse order is",sorted(list1,reverse=True))
# list()--it converts the iterale objects in list like string,tuple,map,dict
str="yogesh"
my_list=list(str)
print(my_list)
my_tuple=("ludo","carrom","snake ladder")
print(type(my_tuple))
mylist=list(my_tuple)
print(mylist)
print(type(mylist))

my_dict={"name":"yogesh","age":22,"per":84.9}
print(my_dict)
# here key of dic are in list:
print(list(my_dict))

#any()-->return true if any element is non-zero otherwise it return false
list1=[2,5,3,7,8,0]
print(any(list1))

#all()--> return true if all element are non zero otherwise return false
list2=[5,3,7,8]
print(all(list2))
list3=[2,5,6,7,0]
print(all(list3))
#



sports = ['cricket', 'football', 'tennis', 'volleyball', 'hockey']
print(max(sports))
print(min(sports))
print(sorted(sports))
print(sorted(sports,reverse=True))

months=["january","may","december","october"]
# max will compare the first letter of every element then give max. so O is max among all.
# max work if all element are of same type same for min
print(max(months))
print(min(months))

# details=["Yogesh",22,89.98]
# print(max(details)) TypeError: '>' not supported between instances of 'int' and 'str'

booleans=[True,False]
print(max(booleans))
print(min(booleans))

myls=['1','2','3']
myintlist=[]
for  i in myls:
     myintlist.append(eval(i))
print(sum(myintlist))