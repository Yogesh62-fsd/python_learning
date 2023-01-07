# Call by Object reference Immutable Types like int,float,str,tuple
def show(a, b):
    a += 1
    b += 1
    print('Inside show function value of a is ', a, 'Value of b is ', b)


a = 20
b = 39
print("Before fn_ call:")
print('value of a is ', a, 'Value of b is ', b)
show(a, b)
print("After fn_ call:")
print('value of a is ', a, 'Value of b is ', b)

# Call by Object reference Mutable Types list
def display(mylist):
    mylist.append(40)

mylist=[10,20,30]
print('Before Fn_CAll: My List is',mylist)
display(mylist)
print('After Fn_CAll: My List is',mylist)