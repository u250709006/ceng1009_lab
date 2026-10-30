# def sumTo(n):
#     total = n * (n + 1) / 2
#     return total
#
# print(sumTo(10))
#
# n = int(input("please enter a number"))
# print("sum is", sumTo(n))




# import turtle
#
#
# def drawStar(t, n, size):
#     angle= 180- 180/n
#     for i in range (n):
#         t.forward(size)
#         t.left(angle)
# wn = turtle.Screen()
# t=turtle.Turtle()
# t.pensize(3)
#
# drawStar(t, 11, 100)
# wn.exitonclick()


# def sumTo(n):
#     total = 0
#     for i in range(1, n+1):
#         total += i
#     return total
#
# print(sumTo(10))
# n=int(input("enter a number"))
# print("sum is", sumTo(n))




# import math
# def mySqrt(x):
#     guess= x / 2
#     for i in range(20):
#         guess= 1 / 2 * (guess + x / guess)
#
#     return guess
#
# n=int(input("enter a positive integer: "))
#
#
# print("The result is", mySqrt(n))
# print("the result is", (math.sqrt(n)))


# import turtle
#
# def drawSprite(someturtle,legs,lenght):
#     angle = 360/legs
#     for i in range(legs):
#
#         someturtle.forward(lenght)
#         someturtle.backward(lenght)
#         someturtle.left(angle)
#
# def fancySquare(t, size):
#      for i in range(4):
#         drawSprite(t, 8 , 20)
#         t.forward(size)
#         t.left(90)
#
#
# screen = turtle.Screen()
# t = turtle.Turtle()
# t.color("hotpink")
# t.pensize(3)
# fancySquare(t, 100)
# screen.exitonclick()



# def checkSign(number):
#     if number > 0:
#         return "positive"
#
#     elif number < 0:
#         return "negative"
#
#     else:
#         return "zero"
#
# numbers=[-7, 5 , 0]
# for number in numbers:
#     print(number, checkSign(number))


# Exercise 7

import turtle


def drawbar(t, height, gap):

    t.penup()
    t.left(90)
    t.fd(height+ gap)
    t.write("" + str(height))
    t.backward(height+ gap)
    t.right(90)
    t.pendown()

    t.begin_fill()
    t.left(90)
    t.forward(height)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()

def barChart(data):
    maxheight = max(data)
    num_bars = len(data)
    border= 10

    gap= (maxheight-border)/25

    wn = turtle.Screen()
    wn.bgcolor("lightgreen")

    right= 40 * num_bars + border
    top = maxheight + 4 * border

    wn.setworldcoordinates(-border,-border,right,top)
    t = turtle.Turtle()
    t.color("blue")
    t.fillcolor("red")
    t.pensize(2)
    for height in data:
        drawbar(t, height, gap)
    wn.exitonclick()

data= [48, 117, 200, 240, 160,240, 220]
barChart(data)

















