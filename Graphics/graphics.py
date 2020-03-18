from turtle import Screen, Turtle

# pip install turtle

screen = Screen()
turtle = Turtle()
turtle.shape("square")

radius = 100
angle = 90

turtle.color("Blue")
turtle.circle(radius, angle)

turtle.begin_fill()
for x in range(4):
    turtle.forward(100)
    turtle.left(90)
turtle.end_fill()



screen.mainloop()

