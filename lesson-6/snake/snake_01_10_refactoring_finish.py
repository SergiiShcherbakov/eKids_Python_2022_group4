import turtle
import time
import random

delay = 0.2

# Score
score = 0
high_score = 0

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

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

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
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def move_snake():
    move_tail()
    move_head()


def move_head():
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


def restart_game():
    global segment, score, delay
    time.sleep(1)
    head.goto(0, 0)
    head.direction = "stop"
    # Hide the segments
    for segment in segments:
        segment.goto(1000, 1000)
    # Clear the segments list
    segments.clear()
    # Reset the score
    score = 0
    # Reset the delay
    delay = 0.2
    print_score()


def is_head_out():
    return head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290


def move_tail():
    global x, y
    # Move the end segment first in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)
        # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)


def print_score():
    pen.clear()
    pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))


def is_food_eaten(head):
    return head.distance(food) < 20


def update_scores():
    global score, high_score
    score += 10
    if score > high_score:
        high_score = score


def create_new_food():
    global x, y
    # move the food to a random spot
    x = random.randint(-285, 285)
    y = random.randint(-285, 285)
    food.goto(x, y)


def add_new_segment():
    new_segment = turtle.Turtle()
    new_segment.speed(0)
    new_segment.shape("square")
    new_segment.color("grey")
    new_segment.penup()
    segments.append(new_segment)


def is_snake_bit_segment(segment, head):
    return segment.distance(head) < 20


while True:
    wn.update()

    if is_head_out():
        restart_game()

    if is_food_eaten(head):
        create_new_food()
        add_new_segment()
        # Shorten the delay
        delay -= 0.001
        update_scores()
        print_score()

    move_snake()

    # Check for head collision with the body segments
    for segment in segments:
        if is_snake_bit_segment(segment, head):
            restart_game()

    time.sleep(delay)
