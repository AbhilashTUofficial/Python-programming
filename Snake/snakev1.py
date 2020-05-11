import turtle
import time
import random

delay = 0.1

# score
score = 0
high_score = 0

# window
win = turtle.Screen()
win.title("Snake game")
win.bgcolor("green")
win.setup(width=600, height=600)
win.tracer(0)

# snake head
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# snake fruit
fruit = turtle.Turtle()
fruit.speed(0)
fruit.shape("circle")
fruit.color("red")
fruit.penup()
fruit.goto(0, 100)

tails = []

# score
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.hideturtle()
pen.goto(0, 200)
pen.write("Score: 0 High Score: 0", align="center", font=("Courier", 24, "normal"))


# move functions
def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)


# keyboard binding

win.listen()
win.onkeypress(go_up, 'w')
win.onkeypress(go_down, "s")
win.onkeypress(go_right, "d")
win.onkeypress(go_left, "a")

# gameloop
while True:
    win.update()
    # collision with border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # hide tails
        for tail in tails:
            tail.goto(1000, 1000)
        # clear the tails
        tails.clear()
        # reset the score
        score = 0
        # reset the delay
        delay = 0.1
        pen.clear()
        pen.write("Score: {} High score {}".format(str(score), str(high_score)), align="center", font=("Courier", 24, "normal"))
        pen.goto(0, 200)

    # check collision with the fruit
    if head.distance(fruit) < 20:
        # move fruit to new random pos
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        fruit.goto(x, y)

        # add new tail
        new_tail = turtle.Turtle()
        new_tail.speed(0)
        new_tail.shape("square")
        new_tail.color("grey")
        new_tail.penup()
        tails.append(new_tail)

        # speed up the snake
        delay -= 0.001
        # increase the score
        score += 1
        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {} High Score: {} ".format(str(score), str(high_score)), align="center",
                  font=("Courier", 24, "normal"))
        pen.goto(0, 200)
    # move the end segments(tails) first in reverse order
    for index in range(len(tails) - 1, 0, -1):
        x = tails[index - 1].xcor()
        y = tails[index - 1].ycor()
        tails[index].goto(x, y)
    # move segment(tail) 0 to where the head is
    if len(tails) > 0:
        x = head.xcor()
        y = head.ycor()
        tails[0].goto(x, y)
    move()

    # check the head collision with the tails
    for tail in tails:
        if tail.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # hide the tails
            for tail in tails:
                tail.goto(1000, 1000)
            # clear the tails
            tails.clear()
            # reset score
            score = 0
            # reset delay
            delay = 0.1
            # update the score display
            pen.clear()
            pen.write("Score: %s High Score: {}".format(str(score), str(high_score)), align="center",
                      font=("Courier", 24, "normal"))
            pen.goto(0, 200)
    time.sleep(delay)
win.mainloop()
