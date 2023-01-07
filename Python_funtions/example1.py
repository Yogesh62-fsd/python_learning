def add(a, b):
    print("values of a is ", a, " and b is", b)
    c = a + b
    print('Their sum is ', c)
# returning the values from fuction
def diff(a, b):
    print("values of a is ", a, " and b is", b)
    return a - b


# a = eval(input('enter the value of a:'))
# b = eval(input("enter the value of b:"))
# add(a, b)
# d = diff(a, b)
# print('Sum is ', d)

def absolute(n):
    if(n>0):
        return n
    else:
        return (-n)
n=eval(input('enter some value:'))
r=absolute(n)
print('Absolute value of n is',r)

# import math
# def absolute(a):
#     return math.fabs(a)
# n=absolute(-9)
# print('Absolute value  is',n)
