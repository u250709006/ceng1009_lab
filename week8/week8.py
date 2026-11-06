# def exam_grades(mark):
#     if mark >= 90:
#         return "A"
#     elif mark >= 80:
#         return "B"
#     elif mark >= 70:
#         return "C"
#     elif mark >= 60:
#         return "D"
#     else :
#         return "F"
#
# marks=[95,98,89.9,80,79.9,70,65,60,59.5,0]
# for mark in marks:
#     print("Grade is",exam_grades(mark))
#
# mark=float(input("Enter mark:"))
# print("grade is",exam_grades(mark))










#Exercise2

# import turtle
#
# def choose_color(height):
#     if height >=200:
#         return "red"
#
#     if  height >=100:
#         return "orange"
#
#     else:
#         return "green"
#
#
# def drawBar(t, height,gap):
#     t.penup()
#     t.left(90)
#     t.fd(height+gap)
#     t.write(" "+str(height))
#     t.backward(height + gap)
#     t.right(90)
#     t.pendown()
#
#     t.fillcolor(choose_color(height))
#     t.begin_fill()
#     t.left(90)
#     t.forward(height)
#     t.right(90)
#     t.forward(40)
#     t.right(90)
#     t.forward(height)
#     t.left(90)
#     t.end_fill()
#
#
# def barChart(data):
#     max_height = max(data)
#     num_bars = len(data)
#     border = 10
#     gap = (max_height + border) / 25
#
#
#
#     wn = turtle.Screen()
#     wn.bgcolor("lightgreen")
#     right = 40 * num_bars + border
#     top = max_height + 4 * border
#     wn.setworldcoordinates(-border, -border, right, top)
#
#
#
#     t= turtle.Turtle()
#     t.color("blue")
#     t.pensize(3)
#
#
#     for height in data:
#         drawBar(t,height,gap)
#
#     wn.exitonclick()
# data=[40,80,100,120,160,200]
# barChart(data)
#
#
#
# Exercise3


# import turtle
#
#
# def chooseColor(height):
#     if height >= 200:
#         return "red"
#     elif height >= 100:
#         return "yellow"
#     else:
#         return "green"
#
#
# def drawBar(t, height, gap):
#     t.penup()
#     t.left(90)
#
#     if height >= 0:
#         t.forward(height + gap)
#     else:
#         t.forward(gap)
#
#     t.write(" " + str(height))
#
#     if height >= 0:
#         t.backward(height + gap)
#     else:
#         t.backward(gap)
#
#     t.right(90)
#     t.pendown()
#
#     t.fillcolor(chooseColor(height))
#     t.begin_fill()
#
#     t.left(90)
#     t.forward(height)
#     t.right(90)
#     t.forward(40)
#     t.right(90)
#     t.forward(height)
#     t.left(90)
#
#     t.end_fill()
#
#
# def barChart(data):
#     max_height = max(0, max(data))
#     min_height = min(0, min(data))
#
#     num_bars = len(data)
#     border = 10
#     gap = (max_height + border) / 25
#
#     wn = turtle.Screen()
#     wn.bgcolor("lightgreen")
#
#     right = 40 * num_bars + border
#     top = max_height + 4 * border
#
#     wn.setworldcoordinates(
#         -border,
#         min_height - border,
#         right,
#         top
#     )
#
#     t = turtle.Turtle()
#     t.color("blue")
#     t.pensize(3)
#
#     for height in data:
#         drawBar(t, height, gap)
#
#         t.penup()
#         t.forward(10)
#         t.pendown()
#
#     wn.exitonclick()


45


#Exercise4

# def findHypot(a,b):
#     c= (a**2 + b**2)**0.5
#     return c
#
# a=float(input("Enter a number:"))
# b=float(input("Enter b number:"))
#
# result=findHypot(a,b)
# print("hypotenuse is ", result)


















