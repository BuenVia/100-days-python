from turtle import Screen
import time
import random
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

pl = Player()
car_manager = CarManager()
score_board = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    screen.listen()
    screen.onkey(pl.move, "Up")

    car_manager.create_car()
    car_manager.move_car()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(pl) < 20:
            game_is_on = False
            score_board.game_over()

    # Detect successful crossing
    if pl.is_at_finish_line():
        pl.goto_start()
        car_manager.level_up()
        score_board.increase_level()


screen.exitonclick()

#TODO Create a turtle that starts at the bottom of the screen and listen for the Up key to move turtle north.
#TODO Create cars 20px x 40px that are randomly generated along the y-axis and move to the left. No cars in top or bottom 50px
#TODO Detect collision between turtle and car - stop game when it happens
#TODO Detect when the turtle reaches the finish line at top (FINISH_LINE_Y) - return turtle to starting pos and increase car speed
#TODO Create a scoreboard to track number of times road crossed. When turtle hits car - Game Over!