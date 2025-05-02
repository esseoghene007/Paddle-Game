from turtle import Turtle

MOVE_DISTANCE = 20

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(position)

    def move_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        new_x = self.xcor()
        self.goto(x=new_x, y=new_y)

    def move_down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        new_x = self.xcor()
        self.goto(x=new_x, y=new_y)