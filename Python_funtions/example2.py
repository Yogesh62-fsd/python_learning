def calculate(a, b):
    return a + b, a - b, a * b, a / b


add,sub, mul, div = calculate(10, 5)
print("Result from calculate is \nadd", add, "\nsub", sub, "\nmul", mul, "\ndiv", div)
print(type(add))
print(type(sub))
print(type(mul))
print(type(div))
# Here the receiving the values in individual variable  so python
# automatically make the datatypes according to that


result=calculate(60,12)
print(result[0],result[1],result[2],result[3])
# If receiving the values in a single variable then python
# automatically make the it's type as tuple
print(type(result))