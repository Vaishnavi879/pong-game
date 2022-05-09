import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

screen=Screen()
screen.bgcolor("black")
screen.setup(height=600,width=800)
screen.title("Pong")
screen.tracer(0)

paddle1=Paddle((-350,0))
paddle2=Paddle((350,0))
ball=Ball()
scoreboard=ScoreBoard()

screen.listen()
screen.onkey(paddle2.move_up,"Up")
screen.onkey(paddle2.move_down,"Down")
screen.onkey(paddle1.move_up,"w")
screen.onkey(paddle1.move_down,"s")


game_is_on=True
while(game_is_on):
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if(ball.ycor() > 280 or ball.ycor() <-280):
        ball.bounce_y()

    if(ball.distance(paddle2)<50 and ball.xcor()>320):
        ball.bounce_x()

    if (ball.distance(paddle1) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    if(ball.xcor()>380):
        ball.reset_position()
        scoreboard.l_point()

    if(ball.xcor()<-380):
        ball.reset_position()
        scoreboard.r_point()


    # hit_paddle1=False
    # hit_paddle2 = False
    # time.sleep(0.1)
    # if(ball.ycor()>330 or ball.ycor()<-330):
    #     ball.change()
    # if (ball.xcor() > 350 or ball.xcor() < -350):
    #     if(ball.distance(paddle1)<15):
    #         ball.change()
    #         hit_paddle1=True
    #         break
    #     if (ball.distance(paddle2) < 15):
    #         ball.change()
    #         hit_paddle2 = True
    #         break
    #     if(hit_paddle1==False):
    #         score_board.scoring2()
    #         ball.new_ball()
    #     elif (hit_paddle2 == False):
    #         score_board.scoring1()
    #         ball.new_ball()
    #
    # ball.move()


screen.exitonclick()