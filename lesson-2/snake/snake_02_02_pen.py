import turtle
import time

delay = 1

# set up the screen
wn = turtle.Screen()
wn.setup(width=600, height=600)
wn.tracer(0)
wn.title("Snake Game by Mahesh Sawant")
wn.bgcolor("green")

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)

while True:
    wn.update()

    pen.clear()
    pen.write("X coord: {}  Y coord: {}".format(55, 33), align="center",
              font=("Courier", 24, "normal"))

    time.sleep(delay)
