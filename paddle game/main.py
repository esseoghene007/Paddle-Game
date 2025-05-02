import turtle
import paddle
import ball
import time 
import scoreboard

screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("The Pin Pong Game")
screen.tracer(0)

r_paddle = paddle.Paddle((350, 0))
l_paddle = paddle.Paddle((-350, 0))
game_ball = ball.Ball()
game_score = scoreboard.Scoreboard()

screen.listen()
screen.onkey(fun=r_paddle.move_up, key="Up")
screen.onkey(fun=r_paddle.move_down, key="Down")
screen.onkey(fun=l_paddle.move_up, key="w")
screen.onkey(fun=l_paddle.move_down, key="s")

is_game_over = False
while not is_game_over:
    time.sleep(0.1)
    screen.update()
    game_ball.move()

    #Detect collision with the wall
    if game_ball.ycor() > 280 or game_ball.ycor() < -280:
        #needs to bounce
        game_ball.bounce_yaxis()

    #Detect collision with both paddles
    if game_ball.distance(r_paddle) < 50 and game_ball.xcor() > 320 or game_ball.distance(l_paddle) < 50 and game_ball.xcor() < -320:
        game_ball.bounce_xaxis()

    #Detect when r_paddle misses the ball
    if game_ball.xcor() > 380:
        game_ball.reset_pos()
        game_score.l_point()
    
    #Detect when l_paddle misses the ball
    if game_ball.xcor() < -380:
        game_ball.reset_pos()
        game_score.r_point()
        


















screen.exitonclick()