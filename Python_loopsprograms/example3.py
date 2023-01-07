
for i in range(10):
    print(i,end=" ")
print()
for i in range(1,10):
    print(i,end=" ")

x=eval(input('enter the number'))
total=0
for i in range(x):
    print(i,end=",")
    total+=i
print()
print("Sum of all the numbers from 1 to {0} is {1}".format(x,total))

