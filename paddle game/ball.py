from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("purple")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_y = self.ycor() + self.y_move
        new_x = self.xcor() + self.x_move
        self.goto(x=new_x, y=new_y)

    def bounce_yaxis(self):
        self.y_move *= -1

    def bounce_xaxis(self):
        self.x_move *= -1
        self.move_speed *= 0.9
    
    def reset_pos(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_xaxis()
        

