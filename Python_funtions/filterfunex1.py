def checknum(n):
    return n%2==0

mynumlist=[2,5,4,6,9,1,11,8]
# filter pass each element of seq to function if fun return true
# for that then it return it that element if false it return then
# it do not return the element.
print(list(filter(checknum,mynumlist)))
for x in filter(checknum,mynumlist):
                print(x)
# Using lambda with filter:

mylist=[2,5,4,6,9,1,11,8]
result=list(filter(lambda num:num%2==0,mylist))
print(result)

# lambda c: (True) if c in ['a','e','i','o','u'] else (False)

name=input('enter your name:')
result=list(filter( lambda c: (True) if c in ['a','e','i','o','u'] else (False),name))

if len(result)==0:
    print('No vowels in your name')
else:
    print('Vowels in your name is ',result)

































