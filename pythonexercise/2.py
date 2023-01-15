# #Create a random list of values such as [True, 1, 5, 0, False, “Python”].
# Try to filter the False or empty values and create new list
# Use filter function with  “None”
my_list=[True, 1, 5, 0, False,'Python']
result=list(filter(lambda a:True if a!=0 and a!=False and a!=None else False,my_list))
print(result)









