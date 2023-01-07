# Write a program to accept five integers from the user ,
# store them in a list .
# Display these integers and also display their sum

mylist=[];
sum=0
for i in range(5):
    n=eval(input('enter the integer:'))
    mylist.append(n)
    sum+=n
print(mylist,"It's Sum is ",sum)
