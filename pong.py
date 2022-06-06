# Pong game

import turtle

wn = turtle.Screen()
wn.title("PONG")
wn.setup(width=800, height=600)
wn.bgcolor("black")
wn.tracer(0)

#Score
scoreA = 0
scoreB = 0

# Paddle A
paddleA = turtle.Turtle()
paddleA.speed(0) # speed of the animation.
paddleA.shape("square")
paddleA.color("red")
paddleA.shapesize(stretch_wid=5, stretch_len=1)
paddleA.penup() # doesnt draw lines
paddleA.goto(-350,0)

# Paddle B
paddleB = turtle.Turtle()
paddleB.speed(0) # speed of the animation.
paddleB.shape("square")
paddleB.color("blue")
paddleB.shapesize(stretch_wid=5, stretch_len=1)
paddleB.penup() # doesnt draw lines
paddleB.goto(350,0)

# Ball
ball = turtle.Turtle()
ball.speed(0) # speed of the animation.
ball.shape("circle")
ball.color("white")
ball.penup() # doesnt draw lines
ball.goto(0,0)
ball.dx = 1.5
ball.dy = 1.5

# Pen for Red
penR = turtle.Turtle()
penR.speed(0)
penR.color("red")
penR.penup()
penR.hideturtle()
penR.goto(-200, 260)
penR.write("Red: 0", font=("Courier", 24, "normal"))

# Pen for Blue
penB = turtle.Turtle()
penB.speed(0)
penB.color("blue")
penB.penup()
penB.hideturtle()
penB.goto(100, 260)
penB.write("Blue: 0", font=("Courier", 24, "normal"))

# Red Bullet
redBullet = turtle.Turtle()
redBullet.speed(0)
redBullet.shapesize(stretch_len=2)
redBullet.color("white")
redBullet.shape("circle")
redBullet.penup()
redBullet.goto(paddleA.xcor(),paddleA.ycor())
redBullet.hideturtle()





# Functions for moving paddles

def paddleA_up(): # paddle A going up
    y = paddleA.ycor()
    y += 40
    paddleA.sety(y)

def paddleA_down(): # paddle A going down
    y = paddleA.ycor()
    y -= 40
    paddleA.sety(y)

def paddleB_up(): # paddle B going up
    y = paddleB.ycor()
    y += 40
    paddleB.sety(y)

def paddleB_down(): # paddle B going down
    y = paddleB.ycor()
    y -= 40
    paddleB.sety(y)

#Functions for shooting

def redShoot():
    redBullet.showturtle()
    redBullet.fd(300)
    redBullet.hideturtle()
    redBullet.backward(300)



# Keyboard binding

wn.listen()
wn.onkeypress(paddleA_up, "w")
wn.onkeypress(paddleA_down, "s")

wn.onkeypress(paddleB_up, "Up")
wn.onkeypress(paddleB_down, "Down")

wn.onkeypress(redShoot, "x")


# Main Game Loop

while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking

    # Top
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    # Bottom
    if ball.ycor() < -280:
        ball.sety(-280)
        ball.dy *= -1

    # Right
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        scoreA += 1
        penR.clear()
        penR.write("Red: {}".format(scoreA), font=("Courier", 24, "normal"))

    # Left
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        scoreB += 1
        penB.clear()
        penB.write("Blue: {}".format(scoreB), font=("Courier", 24, "normal"))

    # Bouncing off the paddle B
    if (ball.xcor() > 327) and (ball.xcor() < 350) and \
       (ball.ycor() < paddleB.ycor() + 40) and (ball.ycor() > paddleB.ycor() - 40):

        ball.setx(327)
        ball.dx *= -1

    # Bouncing off the paddle B
    if (ball.xcor() < -327) and (ball.xcor() > -350) and \
       (ball.ycor() < paddleA.ycor() + 40) and (ball.ycor() > paddleA.ycor() - 40):

        ball.setx(-327)
        ball.dx *= -1



