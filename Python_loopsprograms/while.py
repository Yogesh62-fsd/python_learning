# # print 1 to n:
# n=eval(input('enter the no:'))
# i=1
# while i<=n:
#     print(i)
#     i+=1
# # sum of n natural no:
# n=eval(input('enter the no:'))
# i=0
# sum=0
# while i<=n:
#     sum+=i
#     i+=1
# print(sum)
row =eval(input('enter the row'))
col =eval(input('enter the col'))
i=0
while i<row:
         j=0
         while j<col:
             if(i==0 or j==0 or i==4 or j==4):
               print("*",end=" ")
             else:
               print(" ",end=" ")
             j+=1
         i+=1
         print()

