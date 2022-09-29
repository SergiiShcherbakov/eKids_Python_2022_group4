import turtle
import time

delay=1

# set up the screen
wn=turtle.Screen()
wn.setup(width=600,height=600)
wn.tracer(0)
wn.title("Snake Game by Mahesh Sawant")
wn.bgcolor("green")

while True:
    wn.update()
    time.sleep(delay)
