def demo(s1, s2):
    s3 = s1 + s2
    print('Joined string ', s3)


demo("Good", "Evening")


# demo("Good") it will give error positional argument: s2 required.
def grocery(productname, productprice):
    print("Product name is ", productname, " Product price is", productprice)

grocery("Bread",120)
grocery(productprice=120,productname="Bread")
print("=========KEYWORD ARGUMENT===============")
def display(num1,num2):
    print("num1 is ",num1,"num2 is ",num2)
display(2,5)
display(num2=5,num1=8)
display(10,num2=6)
# display(num2=6,56) keyword argument must be followed by postional argument.

