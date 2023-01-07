# age=eval(input('enter your age'))
# msg='not eligible for vote'if age<18 else 'eligible for vote'
# print(msg)
# #----------Checking even and odd using single line if else
# no=eval(input('enter the no:'))
# result='Even no' if no%2==0 else 'Odd no'
# print("{0} No is ".format(no),result)
#---------------------------------------------
age=eval(input('enter your age'))
msg='kid' if age<13 else 'Teenager' if age<20 else'Adult'
print(msg)

number=eval(input('enter the number:'))
result=('even')if(number%2==0)else('odd')
print('Number is {0}, It is {1}'.format(number,result))