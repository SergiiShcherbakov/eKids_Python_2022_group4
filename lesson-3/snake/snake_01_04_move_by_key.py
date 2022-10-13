import turtle
import time

delay = 0.1

# set up the screen
wn=turtle.Screen()
wn.setup(width=600, height=600)
wn.tracer(0)
wn.title("Snake Game by Mahesh Sawant")
wn.bgcolor("green")

# Snake head
head=turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction="stop"

# Pen
pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)

# Functions
def go_up():
    y = head.ycor()
    head.sety(y + 20)

def go_down():
    y = head.ycor()
    head.sety(y - 20)

def go_left():
    x = head.xcor()
    head.setx(x - 20)

def go_right():
    x = head.xcor()
    head.setx(x + 20)

# def any_key_down():
#     pen.clear()
#     pen.write("works")

# keyboard bindings
wn.listen()
wn.onkeypress(go_up,"Up")
wn.onkeypress(go_down,"Down")
wn.onkeypress(go_left,"Left")
wn.onkeypress(go_right,"Right")
# wn.onkeypress(any_key_down)

while True:
    wn.update()

    pen.clear()
    pen.write("X coord: {}  Y coord: {}".format(head.xcor(), head.ycor()), align="center",
              font=("Courier", 24, "normal"))

    time.sleep(delay)