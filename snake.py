from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
RIGHT = 0
DOWN = 270
LEFT = 180

class Snake:

    def __init__(self):
        self.turtles = []
        self.create_snake()
        x_coordinate = 0
        self.head = self.turtles[0]

    def create_snake(self):
        x_coordinate = 0
        # Create Three squares (3 turtles) - 20x20
        for i in range(0, 3):
            new_turtle = Turtle()
            new_turtle.penup()
            new_turtle.shape("square")
            new_turtle.color("white")
            new_turtle.setposition(x=x_coordinate, y=0)
            x_coordinate -= 20
            self.turtles.append(new_turtle)

    def move(self):
        # End of snake follows first segments
        for seg_num in range(len(self.turtles) - 1, 0, -1):
            new_x = self.turtles[seg_num - 1].xcor()
            new_y = self.turtles[seg_num - 1].ycor()
            self.turtles[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
