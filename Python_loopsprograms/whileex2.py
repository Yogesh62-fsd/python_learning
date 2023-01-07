from random import randint
a=randint(1,200)
print("Random number is {0}".format(a))
while True:
    n=eval(input('Guess the no and enter it'))
    if(a==n):
        print('Congratulation! You guessed it right')
        break
    elif( n<=0):
         print('Thankyou ')
         break
    elif (n>a):
        print('Your Guess Number is too Large')
    elif (n<a):
        print('Your Guess Number is too Small')
