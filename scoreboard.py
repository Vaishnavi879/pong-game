from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score1=0
        self.score2=0
        self.update()

    def update(self):
        self.goto(-100, 200)
        self.write(self.score1, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.score2, align="center", font=("Courier", 80, "normal"))

    def l_point(self):
        self.clear()
        self.score1+=1
        self.update()

    def r_point(self):
        self.clear()
        self.score2+=1
        self.update()



    # def center_line(self):
    #     for _ in range(0,10):
    #         self.pendown()
    #         self.forward(30)
    #         self.penup()
    #         self.forward(30)
    #


    # def scoring1(self):
    #     self.clear()
    #     self.score1 +=1
    #     self.write(f"{self.score1}  {self.score2}",False,"center",("Arial",30,"normal"))
    #
    # def scoring2(self):
    #     self.clear()
    #     self.score2 +=1
    #     self.write(f"{self.score1}  {self.score2}",False,"center",("Arial",30,"normal"))
