# s="I love Pyhton"
# def show():
#     print(s)
#     print(p)
# p="I love Java"
# show()

# d="I Love Python"
# def f():
#     s="I love c"
#     print(s)
# f()
s="I Love Python"
def f():
    # print(s)
    global s
    s="I love c"
    print(s)
f()
print(s)

