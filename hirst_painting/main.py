import random
import turtle as t

t.colormode(255)
tim = t.Turtle()
tim.hideturtle()
tim.speed('fastest')
color_list = [(232, 240, 235), (225, 233, 238), (237, 34, 109), (153, 24, 65), (240, 73, 34), (7, 147, 92), (218, 170, 46), (179, 158, 44), (25, 123, 190), (44, 190, 232)]

# 10 x 10 rows of dots - 20 in size and 50 in space
tim.penup()
tim.setheading(255)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    # print(color(color_list))
    tim.pendown()
    tim.dot(20, random.choice(color_list))
    tim.penup()
    tim.fd(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.fd(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = t.Screen()
screen.exitonclick()
