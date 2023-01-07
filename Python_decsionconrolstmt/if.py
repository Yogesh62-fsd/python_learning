# wap to check whether a no is even or odd
n=eval(input('enter a no :'))
if(n%2==0):
     print("no is even")
if(n%2!=0):
     print("no is odd")
#or only when body of if stmt contain only one stmt after it
if(n%2==0):print("no is even")
if(n%2!=0):print("no is odd")
# if we want to write multiple line after it then we can use ; as separator
if(n%2==0):print("no is even");print('Hello')
if(n%2!=0):print("no is odd");print('Hi')
