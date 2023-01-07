def square(n):
    return n ** 2


mylist = [1, 2, 3, 4, 5]
for x in mylist:
    print(square(x))
# Same using map function'
sqrnum = map(square, mylist)
print(sqrnum)
# map return the map object so convert it into actual number we have pass it list function
sqrnumlist = list(sqrnum)
print(sqrnumlist)

# or
sqrnum = list(map(square, mylist))
print(sqrnum)
# or
print(list(map(square, mylist)))
# or
for i in map(square, mylist):
    print(i)


def inspect(s):
    if 0 == len(s) % 2:
        return 'even'
    else:
        return s[0]


mynameslist = ['yogesh', 'Praveen', 'Raj']
print(list(map(inspect, mynameslist)))

# Using lambda with map

mylist=[1,2,3,4,5]
result=list(map(lambda num:num*num,mylist))
print(result)

months=['January','February','March']
result=list(map(lambda m:m[0],months))
print(result)
for i in map(lambda m:m[0],months):
    print(i)


names=['Yogesh','Sachin','Raj','Satwick','Shubham']
print(list(map(lambda m:('Even')if len(m)%2==0 else (m[0]),names)))