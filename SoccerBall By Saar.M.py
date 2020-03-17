import turtle

###game window
wn = turtle.Screen()
wn.title("SoccerBall By Saar.M")
wn.bgcolor("blue")
wn.setup(width= 800 , height= 600)
wn.tracer(0)


score_a = 0
score_b = 0

###Player a
player_a = turtle.Turtle()
player_a.speed(0)
player_a.shape("circle")
player_a.color("yellow")
player_a.penup()
player_a.goto(-300 , 0)


def player_a_up():
    y = player_a.ycor()
    y+=20
    player_a.sety(y)

def player_a_down():
    y = player_a.ycor()
    y-=20
    player_a.sety(y)

def player_a_right():
    x = player_a.xcor()
    x+=20
    player_a.setx(x)

def player_a_left():
    x = player_a.xcor()
    x-=20
    player_a.setx(x)

###player b
player_b = turtle.Turtle()
player_b.speed(0)
player_b.shape("circle")
player_b.color("green")
player_b.penup()
player_b.goto(300 , 0)


def player_b_up():
    y = player_b.ycor()
    y+=20
    player_b.sety(y)

def player_b_down():
    y = player_b.ycor()
    y-=20
    player_b.sety(y)

def player_b_right():
    x = player_b.xcor()
    x+=20
    player_b.setx(x)

def player_b_left():
    x = player_b.xcor()
    x-=20
    player_b.setx(x)



###GoalPost_a
GoalPost_a = turtle.Turtle()
GoalPost_a.speed(0)
GoalPost_a.shape("square")
GoalPost_a.color("white")
GoalPost_a.penup()
GoalPost_a.shapesize(stretch_wid= 5 , stretch_len= 1)
GoalPost_a.goto(-350 , 0)

###GoalPost b
GoalPost_b = turtle.Turtle()
GoalPost_b.speed(0)
GoalPost_b.shape("square")
GoalPost_b.color("white")
GoalPost_b.penup()
GoalPost_b.shapesize(stretch_wid= 5 , stretch_len= 1)
GoalPost_b.goto(350 ,0)


###ScoreBoard
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0 , 260)
pen.write("Player A : 0 Player B : 0 "  , align="center", font=("Courier", 25, "bold"))


###keyboard commands
wn.listen()
wn.onkeypress(player_a_up,"w")
wn.onkeypress(player_a_left,"a")
wn.onkeypress(player_a_down,"s")
wn.onkeypress(player_a_right , "d")
wn.onkeypress(player_b_up,8)
wn.onkeypress(player_b_left,4)
wn.onkeypress(player_b_down,5)
wn.onkeypress(player_b_right ,6)

while True:
    wn.update()

    ###scoring

    if (player_a.xcor() > 340 and player_a.xcor() < 361) and (player_a.ycor() < 50 and player_a.ycor() > -50):
        player_a.goto(-300, 0)
        player_b.goto(300, 0)
        score_a+=1
        pen.clear()
        pen.write("Player A: {} Player B: {} ".format(score_a, score_b), align="center",font=("Courier", 25, "bold"))


    if (player_b.xcor() < -340 and player_b.xcor() > -361) and (player_b.ycor() < 50 and player_b.ycor() > -50):
        player_a.goto(-300, 0)
        player_b.goto(300, 0)
        score_b+=1
        pen.clear()
        pen.write("Player A: {} Player B: {} ".format(score_a, score_b), align="center",font=("Courier", 25, "bold"))


    ###players collision
    if player_a.xcor() == player_b.xcor() and player_a.ycor() == player_b.ycor():
        player_a.goto(-300,0)
        player_b.goto(300,0)
        score_a-=1
        score_b-=1
        pen.clear()
        pen.write("Player A: {} Player B: {} ".format(score_a, score_b), align="center",font=("Courier", 25, "bold"))


