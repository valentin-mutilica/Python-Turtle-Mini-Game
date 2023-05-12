import turtle
import random

class Screen:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.title("Turtly Game")
        self.screen.bgcolor("White")
        self.screen.setup(width=600, height=600)


class Turtly:
    def __init__(self):
        self.Turtly = turtle.Turtle()
        self.Turtly.color("green")
        self.Turtly.shape("turtle")
        self.Turtly.penup()
        self.Turtly.speed(0)

    def move_up(self):
        if self.Turtly.ycor() < 280:
            self.Turtly.setheading(90)
            self.Turtly.forward(20)

    def move_down(self):
        if self.Turtly.ycor() > -270:
            self.Turtly.setheading(270)
            self.Turtly.forward(20)

    def move_left(self):
        if self.Turtly.xcor() > -280:
            self.Turtly.setheading(180)
            self.Turtly.forward(20)

    def move_right(self):
        if self.Turtly.xcor() < 280:
            self.Turtly.setheading(0)
            self.Turtly.forward(20)

class Snack:
    def __init__(self):
        self.Snack = turtle.Turtle()
        self.Snack.color("orange")
        self.Snack.shape("circle")
        self.Snack.penup()
        self.Snack.speed(0)
        self.Snack.goto(random.randint(-280, 280), random.randint(-280, 280))

    def is_collision(self, t1, t2):
        distance = t1.distance(t2)
        if distance < 20:
            return True
        else:
            return False
            
           
    def move_randomly(self):
        x_offset = random.randint(-15, 15)
        y_offset = random.randint(-15, 15)
        new_x = self.Snack.xcor() + x_offset
        new_y = self.Snack.ycor() + y_offset
        
        # check if new position is within screen bounds
        if new_x > 280 or new_x < -280:
            new_x = self.Snack.xcor()
        if new_y > 280 or new_y < -280:
            new_y = self.Snack.ycor()
            
        self.Snack.goto(new_x, new_y)

class Score:
    def __init__(self):
        self.score = 0
        self.score_pen = turtle.Turtle()
        self.score_pen.color("black")
        self.score_pen.penup()
        self.score_pen.hideturtle()
        self.score_pen.goto(0, 260)
        self.score_pen.write("Score: {}".format(self.score), align="center", font=("Arial", 16, "normal"))

    def update_score(self):
        self.score += 5
        self.score_pen.clear()
        self.score_pen.write("Score: {}".format(self.score), align="center", font=("Arial", 16, "normal"))

class Game:
    def __init__(self):
        self.screen = Screen()
        self.Turtly = Turtly()
        self.Snack = Snack()
        self.score = Score()

        # Set up the keyboard bindings
        self.screen.screen.listen()
        self.screen.screen.onkeypress(self.Turtly.move_up, "Up")
        self.screen.screen.onkeypress(self.Turtly.move_down, "Down")
        self.screen.screen.onkeypress(self.Turtly.move_left, "Left")
        self.screen.screen.onkeypress(self.Turtly.move_right, "Right")

    def start(self):
        while True:
            if self.score.score == 20:
                break

            # Check for collision
            if self.Snack.is_collision(self.Turtly.Turtly, self.Snack.Snack):
                self.score.update_score()
                self.Snack.Snack.goto(random.randint(-280, 280), random.randint(-280, 280))


            # Move the Snack randomly
            self.Snack.move_randomly()
            
            # Update the screen
            self.screen.screen.update()

        # Game over
        self.game_over_pen = turtle.Turtle()
        self.game_over_pen.color("red")
        self.game_over_pen.penup()
        self.game_over_pen.hideturtle()
        self.game_over_pen.goto(0, 0)
        self.game_over_pen.write("Congratulations, you have won!", align="center", font=("Arial", 24, "normal"))

Game().start()
turtle.mainloop()