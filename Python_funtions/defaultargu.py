def show(name, msg="Hello How are you?"):
    print(name, msg)
# here msg value is default argument if we do not pass then by default it will be passed.

show("yogesh")
show("Sachin", "How do you do?")

def display(a=0,b=20,c=30):
    print(a,b,c)
display(4)
display(4,5)
# display(1,,3) if we are skipping the argument then must all argument after it.
# Solution to this is to use Keyword argument
display(4,c=6)

from math import pow
def calcuate_Area(radius,pi=3.14):
    area=3.14*pow(radius,2)
    print('Area of circle ',area)
radius=eval(input('enter the radius of circle:'))
calcuate_Area(radius)

def varlenarg(*a):
    print(a)
    return a
a=varlenarg(6,7,9,8,0)
print(a)
print(type(a))

def findlargest(*months):
     max=0
     largest=""
     for i in months:
      if len(i)>max:
         max=len(i)
         largest=i
     print('largest Months is ',largest)
findlargest('January','february','March','April','May')

def addnos(n,*a,m):
    sum=n+m
    for i in a:
        sum+=i
    return sum
print(addnos(10,20,30,40,50,m=60))
