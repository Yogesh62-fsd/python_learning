# for i in range(1,5):
#     for j in range(1,4):
#         print('*',end=" ")
#    print()
#
# for i in range(1,5):
#     for j in range(1,4):
#         print("*",end=" ")
#     print()

# *
# * *
# * * *
# * * * *
# * * * * *
for i in range(1,6):
    for j in range(i):
          print("*",end=" ")
    print()
print("--------------------------")
# * * * * *
# * * * *
# * * *
# * *
# *
for i in range(5,0,-1):
    for j in range(i):
          print("*",end=" ")
    print()
print("--------------------------")
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
for i in range(1,7):
      for j in range(1,i):
          print(j,end=" ")
      print()
print("---------------------------")
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
for i in range(6):
    for j in range(i):
        print(i,end=" ")
    print()
print("------------------------------")
# A
# A B
# A B C
# A B C D
# A B C D E
for i in range(65,71):
    for j in range(65,i):
        print(chr(j),end=" ")
    print()
print("------------------------------")
# A
# B B
# C C C
# D D D D
# E E E E E
for i in range(65,70):
    for j in range(64,i):
        print(chr(i),end=" ")
    print()
print("---------------------------------")
# * * * * *
# *       *
# *       *
# *       *
# * * * * *
for i in range(1,6):
    for j in range(1,6):
        if(i==1 or j==1 or i==5 or j==5):
            print('*',end=" ")
        else:
            print(" ",end=" ")
    print()