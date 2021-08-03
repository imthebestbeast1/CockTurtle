from turtle import *

#calls every turtle object and sets anything important to drawing the cock

speed(7)
ball1 = Turtle()
ball2 = Turtle()
bshaft = Turtle()
xtra = Turtle() #used for any extra drawing stuff such as veins or other inconspicuous liquids
xtra.hideturtle()
xtra.penup()
color('black')
ball1.speed(0)
ball2.speed(0)
ball1.begin_fill()
ball2.begin_fill()
sety(40) #setting the main line to the top of the shaft so i dont have extra shitz

#ignore all the lines calling the same methods with different objects
#idfk how to group the bitches

def spurt(x, y, direction, length = 20):
    xtra.goto(x, y)
    xtra.pendown()
    if direction == 'left':
        for i in range(0, length):
            xtra.forward(1)
            xtra.left(2)
        xtra.penup()
        xtra.setheading(0)
        return
    for i in range(0, length):
        xtra.forward(1)
        xtra.right(2)
    xtra.penup()
    xtra.setheading(0)


bshaft.sety(-40)
while True:
    forward(10)
    bshaft.forward(10)
    ball1.forward(120)
    ball1.left(170)
    ball1.forward(10)
    ball1.left(120)
    #i draw the nutz like this to simulate the hair
    #looking for better geometry for hairy balls, this is the best so far
    ball2.forward(120)
    ball2.right(170)
    ball2.forward(10)
    ball2.right(120)

    #prime example of several obj with same methods

    if abs(ball1.pos()) < 1:
        break
left(90)
forward(16)
right(90)
headDegree = 0
while True:
    right(1)
    forward(1)
    headDegree = headDegree + 1
    #finds position at 90 degrees to later shift main line to draw tip
    if headDegree == 90:
        tip = pos()
    if headDegree == 180:
        break
right(90)
forward(16)
ball1.end_fill()
ball2.end_fill()
bshaft.hideturtle()

#Drawing tip

penup() #stops annoying line when moving main line
goto(tip)
left(90)
forward(15)

spurt(470, 10, 'left')
spurt(450, 20, 'left')
spurt(440, -10, 'right')
spurt(470, -5, 'right')

done()