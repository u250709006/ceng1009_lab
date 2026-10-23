import turtle
#--setup--

wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle()

# --Functions--

def drawPoly(someturtle,somesides,somesize):
    angle= 360/somesides
    for i in range(somesides):
        someturtle.forward(somesize)
        someturtle.left(angle)



def drawspiral(someturtle,angle,):
    size=1
    for i in range(100):
        someturtle.forward(size)
        someturtle.right(angle)
        size= size+2

def drawEquitriangle(someturtle,somesize):
    drawPoly(someturtle,3,somesize)

def drawstar(someturtle,size):
    for i in range(5):
        someturtle.forward(size)
        someturtle.right(144)

def drawsprite(someturtle, legs, lenght):
    angle= 360/legs
    for i in range(legs):
        someturtle.forward(lenght)
        someturtle.backward(lenght)
        someturtle.left(angle)





#--exercises--

#Exercises 1

# tess.color("hotpink")
# drawPoly(tess, 8, 50)
# wn.exitonclick()



#Exercise 2

# tess.color("blue")
# for i in range(20):
#     drawPoly(tess,4,100)
#     tess.left(18)
# wn.exitonclick()



#Exersice 3


# tess.color("blue")
# tess.penup()
# tess.goto(-150,0)
# tess.pendown()
# drawspiral(tess,90)
#
#
# tess.penup()
# tess.goto(150,0)
# tess.pendown()
# drawspiral(tess,89)
# wn.exitonclick()


#Exercise 4

#drawEquitriangle(tess, 100)
#wn.exitonclick()

#Exersice 5

# tess.color("hotpink")
# for i in range(5):
#     drawstar(tess,50)
#     tess.penup()
#     tess.fd(200)
#     tess.right(144)
#     tess.pendown()
#
# wn.exitonclick()


#Exercise 6
drawsprite(tess,15,120)
wn.exitonclick()