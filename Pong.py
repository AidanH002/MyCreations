import turtle

wn = turtle.Screen()
wn.title("Pong By @Swerfie")
wn.bgcolor("DarkGray")
wn.setup(width=1200, height=600)
wn.tracer(0)
# Score
score_a = 0
score_b = 0
# Button
pen2 = turtle.Turtle()
pen2.hideturtle
pen2.pencolor("DarkRed")
pen2.color

Button_x = -25
Button_y = 200
ButtonLength = 75
ButtonWidth = 45

mode = 'dark'

# Paddle 1
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.color("darkred")
paddle_1.shapesize(stretch_wid=5, stretch_len=1)
paddle_1.penup()
paddle_1.goto(-550, 0)
# Paddle 2
paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.color("darkred")
paddle_2.shapesize(stretch_wid=5, stretch_len=1)
paddle_2.penup()
paddle_2.goto(550, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("darkred")
ball.shapesize(stretch_wid=1, stretch_len=1)
ball.penup()
ball.goto(0, 0)
ball.dx = .19
ball.dy = .19
ball.dx -= .19
ball.dy -= .19

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.color("lightgray")
pen.write("Player 1: 0  Player 2: 0", align="center", font=("courier", 24, "normal"))

# Draw Border
wall = turtle.Turtle()
wall.penup()
wall.speed(0)
wall.hideturtle()
wall.goto(-602, 305)
wall.pendown()
wall.pensize(width=12)
wall.color("black")
wall.fd(1200)
wall.right(90)
wall.fd(600)
wall.right(90)
wall.fd(1200)
wall.right(90)
wall.fd(600)
wall.penup()

# Display Controls
rules = turtle.Turtle()
rules.penup()
rules.speed(0)
rules.hideturtle()
rules.goto(-802, 0)
rules.write("Player 1 Up: W\nPlayer 1 Down: S\n\nPlayer 2 Up: -\nPlayer 2 Down: +", align="center", font=("courier", 24, "bold"))

# Function
def paddle_1_up():
    y = paddle_1.ycor()
    y += 20
    paddle_1.sety(y)


def paddle_1_down():
    y = paddle_1.ycor()
    y -= 20
    paddle_1.sety(y)


def paddle_2_up():
    y = paddle_2.ycor()
    y += 20
    paddle_2.sety(y)


def paddle_2_down():
    y = paddle_2.ycor()
    y -= 20
    paddle_2.sety(y)


def draw_button(pen2, message='Play?'):
    pen2.hideturtle()
    pen2.penup()
    pen2.begin_fill()
    pen2.goto(Button_x, Button_y)
    pen2.goto(Button_x + ButtonLength, Button_y)
    pen2.goto(Button_x + ButtonLength, Button_y + ButtonWidth)
    pen2.goto(Button_x, Button_y + ButtonWidth)
    pen2.goto(Button_x, Button_y)
    pen2.end_fill()
    pen2.goto(Button_x + 15, Button_y + 15)
    pen2.write(message, font=('courier', 15, 'bold'))


draw_button(pen2)


def button_click(x, y):
    if Button_x <= x <= Button_x + ButtonLength:
        if Button_y <= y <= Button_y + ButtonWidth:
            pen2.clear()
            ball.dx += .19
            ball.dy += .19


wn.onclick(button_click)



# keyboard binding
wn.listen()
wn.onkeypress(paddle_1_up, "w")
wn.onkeypress(paddle_1_down, "s")
wn.onkeypress(paddle_2_up, "-")
wn.onkeypress(paddle_2_down, "+")
# main game loop
while True:
    wn.update()

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -280:
        ball.sety(-280)
        ball.dy *= -1

    if ball.xcor() > 590:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player 1: {}  Player 2: {}".format(score_a, score_b), align="center", font=("courier", 24, "normal"))

    if ball.xcor() < -590:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player 1: {}  Player 2: {}".format(score_a, score_b), align="center", font=("courier", 24, "normal"))

    if paddle_1.ycor() < -235:
        paddle_1.sety(-235)

    if paddle_1.ycor() > 240:
        paddle_1.sety(240)

    if paddle_2.ycor() < -235:
        paddle_2.sety(-235)

    if paddle_2.ycor() > 240:
        paddle_2.sety(240)

    # Paddle and ball collisions
    if ball.xcor() > 520 and (ball.ycor() < paddle_2.ycor() + 40 and ball.ycor() > paddle_2.ycor() - 40):
        ball.setx(510)
        ball.dx *= -1

    if ball.xcor() < -520 and (ball.ycor() < paddle_1.ycor() + 40 and ball.ycor() > paddle_1.ycor() - 40):
        ball.setx(-510)
        ball.dx *= -1
