import turtle
import time

delay = 0.1

# set up the screen
wn = turtle.Screen()
wn.setup(width=600, height=600)
wn.tracer(0)
wn.title("Snake Game by Mahesh Sawant")
wn.bgcolor("green")

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)


# Functions
def go_up():
    head.direction = "up"


def go_down():
    head.direction = "down"


def go_left():
    head.direction = "left"


def go_right():
    head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


# keyboard bindings
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

while True:
    wn.update()

    # Check for a collision with the border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # Reset the delay
        delay = 0.1

    move()

    pen.clear()
    pen.write("X : {}  Y : {} direct : {}".format(head.xcor(), head.ycor(), head.direction), align="center",
              font=("Courier", 24, "normal"))

    time.sleep(delay)
