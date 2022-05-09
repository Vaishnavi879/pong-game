from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.create(position)

    def create(self,position):
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(position)

    def move_up(self):
        new_y=self.ycor()+50
        self.goto(self.xcor(),new_y)

    def move_down(self):
        new_y=self.ycor()-50
        self.goto(self.xcor(),new_y)

