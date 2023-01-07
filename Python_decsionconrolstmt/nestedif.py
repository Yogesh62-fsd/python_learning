a=eval(input('enter the first no:'))
b=eval(input('enter the second no:'))
c=eval(input('enter the third no:'))
if(a>b):
    if(a>c):
        print('a is greater %d'%a)
    else:
        print('c is greater %d'%c)

else:
    if(b>c):
        print('b is greater %d'%b)
    else:
        print('c is greater %d'%c)
