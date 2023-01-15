for i in range(5):
    for j in range(i + 1):
        print("*", end=" ")
    print()
print("============================================")
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
for i in range(1, 7):
    for j in range(1, i):
        print(j, end=" ")
    print()
print("============================================")
for i in range(6, 1, -1):
    for j in range(1, i):
        print(j, end=" ")
    print()
print("============================================")
for i in range(65, 71):
    for j in range(65, i):
        print(chr(j), end=" ")
    print()
print("============================================")
for i in range(70, 64, -1):
    for j in range(65, i):
        print(chr(j), end=" ")
    print()
print("===================================")
for i in range(2,7):
    for j in range(i-1):
        if((i+j)%2==0):
            print("1",end="")
        else:
            print("0",end="")
    print()