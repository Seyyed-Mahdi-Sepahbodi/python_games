import os
import turtle


class Player:

    def __init__(self, x_cordination):

        # create players's paddles and define a score variable for them
        self.paddle = turtle.Turtle()
        self.paddle.speed(0)
        self.paddle.shape("square")
        self.paddle.color("white")
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.penup()
        self.paddle.goto(x_cordination, 0)
        self.score = 0

    def move_up(self):
        y = self.paddle.ycor()
        y += 20
        self.paddle.sety(y)

    def move_down(self):
        y = self.paddle.ycor()
        y -= 20
        self.paddle.sety(y)


class GameLogic:

    def __init__(self, *args, **kwargs):

        # main window of the game
        self.window = turtle.Screen()
        self.window.title("Pong by Seyyed Mahdi Sepahbodi")
        self.window.bgcolor("black")
        self.window.setup(width=800, height=600)
        self.window.tracer(0)

        # create the ball
        self.ball = turtle.Turtle()
        self.ball.speed(0)
        self.ball.shape("square")
        self.ball.color("white")
        self.ball.penup()
        self.ball.goto(0, 0)
        self.ball.dx = 0.03
        self.ball.dy = 0.03

        # create a pen object for writing text in the above of the window that shows result of the game
        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.pen.color("white")
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.goto(0, 260)
        self.pen.write("Player A: 0  Player B: 0",
                       align="center", font=("Courier", 24, "normal"))

    def move_ball(self):
        self.ball.setx(self.ball.xcor() + self.ball.dx)
        self.ball.sety(self.ball.ycor() + self.ball.dy)

    def chack_hitting_border(self):
        if self.ball.ycor() > 290:
            self.ball.sety(290)
            self.ball.dy *= -1
            os.system("aplay ./Pong/ball_sound.wav&")
        elif self.ball.ycor() < -290:
            self.ball.sety(-290)
            self.ball.dy *= -1
            os.system("aplay ./Pong/ball_sound.wav&")

    def check_ball_go_out(self, player1, player2):
        if self.ball.xcor() > 390:
            self.ball.goto(0, 0)
            self.ball.dx *= -1
            player1.score += 1
            self.pen.clear()
            self.pen.write("Player A: {}  Player B: {}".format(
                player1.score, player2.score), align="center", font=("Courier", 24, "normal"))
        elif self.ball.xcor() < -390:
            self.ball.goto(0, 0)
            self.ball.dx *= -1
            player2.score += 1
            self.pen.clear()
            self.pen.write("Player A: {}  Player B: {}".format(
                player1.score, player2.score), align="center", font=("Courier", 24, "normal"))

    def check_hitting_paddle(self, player1, player2):
        if (self.ball.xcor() < -340 and self.ball.xcor() > -350) and (self.ball.ycor() < player1.paddle.ycor() + 40 and self.ball.ycor() > player1.paddle.ycor() - 40):
            self.ball.setx(-340)
            self.ball.dx *= -1
            os.system('aplay ./Pong/ball_sound.wav&')
        elif (self.ball.xcor() > 340 and self.ball.xcor() < 350) and (self.ball.ycor() < player2.paddle.ycor() + 40 and self.ball.ycor() > player2.paddle.ycor() - 40):
            self.ball.setx(340)
            self.ball.dx *= -1
            os.system('aplay ./Pong/ball_sound.wav&')


class StartGame:

    def __init__(self, *args, **kwargs):
        game = GameLogic()
        player1 = Player(-350)
        player2 = Player(350)

        # keyboard binding
        game.window.listen()
        game.window.onkeypress(player1.move_up, "w")
        game.window.onkeypress(player1.move_down, "s")
        game.window.onkeypress(player2.move_up, "Up")
        game.window.onkeypress(player2.move_down, "Down")

        while True:
            game.window.update()
            game.move_ball()
            game.chack_hitting_border()
            game.check_ball_go_out(player1, player2)
            game.check_hitting_paddle(player1, player2)


start = StartGame()
