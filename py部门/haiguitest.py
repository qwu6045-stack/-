import turtle
import math

tt = turtle.Turtle()
tt.speed(0)
tt.hideturtle()


screen = turtle.Screen()
screen.setup(600,600)
screen.tracer()

r1 = 300.0
r2 = 175.0
r3 = 5.0

t,count = 0,0
points = []
def yuanheart(x,y,r):
    tt.penup()
    tt.goto(x,y-r)
    tt.pendown()
    tt.circle(r)

yuanheart(0,0,r1)

def xiaoyuan():
    prop = 0.9
    global t,count,points
    ti = -((r1-r2)/r2)*t
    if count >= 100:
        return
    x2 = (r1-r2)*math.cos(t)
    y2 = (r1-r2)*math.sin(t)
    x3 = 







turtle.done()