
# a=range(12)
# print(a)
# for i in a:
#     print(i)

# b=range(1,10)
# print(b)
# for i in b:
#      print(i)

# c=range(1,10,2)
# print(c)
# for i in c:
#      print(i)
b=range(-10,-1) # range fun only moves forward
# and -1 comes right side of start value so it will print -10 to -2
print(b)
for i in b:
     print(i)
b=range(-10,-21)
# range fun only moves forward and 1 does't comes
# right of -10 so output is blank
print(b)
for i in b:
     print(i)

# syntax of range range(start,end,step)
for i in range(1,10,2):
    print(i,end=" ")
