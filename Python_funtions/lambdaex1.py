def sum(a,b):
    return a+b
result=sum(4,6)
print(result)
# lambda as anoymous function
print((lambda a,b:a+b)(4,5))
# lambda as by assign as variable
sum=lambda a,b:a+b
print(sum(5,6))

firstcharacter=lambda s:s[0]
print('First Character of Bhopal is ',firstcharacter("Bhopal"))
lastcharacter=lambda s:s[-1]
# or  lastcharacter=lambda s:s[len(s)-1]
print('Last Character of Bhopal is',lastcharacter("Bhopal"))

# result=lambda n: ("even")if n%2==0 else("Odd")
result=lambda n:n%2==0
print("Number is even ",result(8))

# Greater among 2

greater=lambda a,b:(a)if a>b else b
a=eval(input('enter first no:'))
b=eval(input('enter second no:'))
print("Greater number is ",greater(a,b))


from turtle import *
# speed(900)
# color("green")
# bgcolor("black")
# b=1200
# while b>0:
#     left(b)
#     forward(b*3)
#     b=b-1
import colorsys
speed(0)
hideturtle()
bgcolor('black')
tracer(5)
width(2)
h=0.001
for i in range(180):
    color(colorsys.hls_to_rgb(h,1,3))
    forward(100)
    left(60)
    forward(100)
    right(120)
    circle(150)
    left(240)
    forward(100)
    left(60)
    forward(100)
    h+=0.02
    color(colorsys.hls_to_rgb(h,1,3))
    forward(100)
    right(60)
    forward(100)
    left(120)
    circle(-50)
    right(240)
    forward(100)
    right(60)
    forward(100)
    left(2)
    h+=0.02

