for i in  range(5,0,-1):
    for j in range(1,6):
        if(j<=i-1):
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print()
#         *
#       * *
#     * * *
#   * * * *
# * * * * *

for i in range(1,6):
    for j in range(1,6):
        if(j<=i-1):
            print(i,end=" ")
        else:
            print(j,end=" ")
    print()
    # 1 2 3 4 5
    # 2 2 3 4 5
    # 3 3 3 4 5
    # 4 4 4 4 5
    # 5 5 5 5 5
for i in range(1,6):
    for j in range(i):
        print(i,end=" ")
    print()
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
count=0
for i in range(1,6):
    for j in range(i):
         count+=1
         print(count,end=" ")
    print()
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15

n=eval(input('enter the n'))
n+=1
for i in range(1,n):
    for j in range(i):
        print("*",end=" ")
        space=2*n-2*i
    for j in range(1,space-1):
         print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()
for i in range(n-1,0,-1):
    for j in range(i):
        print("*",end=" ")
        space=2*n-2*i
    for j in range(1,space-1):
         print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()
# *             *
# * *         * *
# * * *     * * *
# * * * * * * * *
# * * * * * * * *
# * * *     * * *
# * *         * *
# *             *

for i in range(6,0,-1):
    for j in range(1,i):
        print(j,end=" ")
    print()

for i in range(1,6):
    for j in range(1,i+1):
        if((i+j)%2==0):
            print("1",end=" ")
        else:
            print("0",end=" ")
    print()
