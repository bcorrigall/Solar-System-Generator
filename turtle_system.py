# one of my first python projects

import turtle
import random
turtle.tracer(0, 0)

turtle.Screen().bgcolor("Black")

# the star
star = turtle.Turtle()
star.hideturtle()
star.speed(10)
star.up()
starcolor = random.choice(["Red","Blue","Orange","Cyan","Turquoise","Yellow","White","Purple","Gold"])
star.begin_fill()
star.fillcolor(starcolor)
star.pencolor(starcolor)
originalstarsize = random.randrange(20,90)
star.goto(0,-originalstarsize)
star.circle(originalstarsize)
star.end_fill()

# the planets
maxplanetnumber = random.randrange(0,10)
planetnumber = 0

cb = turtle.Turtle()
cb.hideturtle()
cb.speed(10)


size = originalstarsize

while planetnumber < maxplanetnumber :
    planetarydistance = random.randrange(15,50)
    cb.up()
    cb.pensize(1)
    cb.pencolor("White")
    cb.goto(0,-size-planetarydistance)
    cb.down()
    cb.circle(size+planetarydistance)
    cb.up()
    cb.goto(size+planetarydistance,0)
    cb.down()
    cb.begin_fill()
    planetcolor = random.choice(["Red","Blue","Grey","Green","Brown","Tan"])
    cb.fillcolor(planetcolor)
    cb.pencolor(planetcolor)
    planetarysize = random.randrange(4,12)
    cb.circle(planetarysize)
    cb.end_fill()

    accessories = random.randrange(0,10)
# the moons
    if 8 <= accessories <= 10 :
        moondistance = random.randrange(4,6)
        cb.up()
        cb.pencolor("White")
        cb.goto(size+planetarydistance,-moondistance)
        cb.down()
        cb.circle(moondistance+planetarysize)
        cb.up()
        cb.goto(size+planetarydistance+moondistance,-moondistance)
        cb.down()
        cb.begin_fill()
        planetcolor = random.choice(["Red","Blue","Grey","Green","Brown"])
        cb.fillcolor(planetcolor)
        cb.pencolor(planetcolor)
        moonsize = random.randrange(2,3)
        cb.circle(moonsize)
        cb.end_fill()

# the rings
    elif accessories == 7 :
        ringdistance = random.randrange(3,5)
        ringwidth = random.randrange(2,3)
        cb.up()
        ringcolor = random.choice(["Red","Blue","Grey","Green","Brown","Orange","Cyan","Turquoise","Yellow","Purple","Gold"])
        cb.pencolor(ringcolor)
        cb.pensize(ringwidth)
        cb.goto(size+planetarydistance,-ringdistance)
        cb.down()
        cb.circle(ringdistance+planetarysize)
        cb.end_fill()
    
    size = planetarydistance+size
    planetnumber = planetnumber+1

turtle.exitonclick()