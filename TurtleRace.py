import random
import turtle
scn = turtle.Screen()
t1 = turtle.Turtle()
t2 = turtle.Turtle()
t1.shape("turtle")
t2.shape("turtle")
t1.fillcolor("red")
t2.fillcolor("blue")
t1.pencolor("white")
t2.pencolor("white")
scn.bgcolor("black")


t1.penup()
t1.goto(-300,300)
t1.goto(300,300)
t1.pendown()
t1.circle(50)
t1.penup()
t1.goto(-300,350)

t2.penup()
t2.goto(-300,-300)
t2.goto(300,-300)
t2.pendown()
t2.circle(50)
t2.penup()
t2.goto(-300,-250)

while t1.pos() < (300,300) and t2.pos() < (300,-300):
    t1.fd(random.randint(0,25))
    t2.fd(random.randint(0,25))

if t1.pos() > (300,300):
    print("Red")
elif t2.pos() > (300,-300):
    print("Blue")

turtle.exitonclick()