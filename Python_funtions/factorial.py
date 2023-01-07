def factorial(n):
    fact=1
    while n>0:
        fact*=n
        n-=1
    return fact
n=eval(input('enter the number to calculate factorial:'))
factno=factorial(n)
print('Number is ',n)
print("It's factorial is ",factno)
print("======================================")

def greet(name):
    print("Hello",name)

x=greet("yogesh")
print('greet returns ',x)
# function returning nothing is will return none

