import pygame
from pygame.locals import *
import random

SIZE = width, height = (800, 800)
ROAD_W = int(width / 1.6)
ROADMARD_W = int(width / 80)
RIGHT_LANE = width / 2 + ROAD_W / 4
LEFT_LANE = width / 2 - ROAD_W / 4
SPEED = 1


pygame.init()
running = True
# set window size
screen = pygame.display.set_mode(SIZE)
# set title
pygame.display.set_caption("Matt's Car Game")
# set background color
screen.fill((60, 220, 0))


# apply changes
pygame.display.update()

# load images
car = pygame.image.load("car.png")
car_loc = car.get_rect()
car_loc.center = RIGHT_LANE, height * 0.8

car_two = pygame.image.load("otherCar.png")
car_two_loc = car_two.get_rect()
car_two_loc.center = LEFT_LANE, height * 0.2

counter = 0
# Game loop
while running:
    counter += 1
    if counter == 5000:
        SPEED += 0.15
        counter = 0
        print(f"Level up! {SPEED}")
    car_two_loc[1] += SPEED
    if car_two_loc[1] > height:
        if random.randint(0, 1) == 0:
            car_two_loc.center = RIGHT_LANE, - 200
        else:
            car_two_loc.center = LEFT_LANE, - 200

    if car_loc[0] == car_two_loc[0] and car_two_loc[1] > car_loc[1] - 250:
        print("GAME OVER! YOU LOST!")
        break

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key in [K_a, K_LEFT]:
                car_loc = car_loc.move([-int(ROAD_W / 2), 0])
            if event.key in [K_d, K_RIGHT]:
                car_loc = car_loc.move([+int(ROAD_W / 2), 0])

    # draw graphics
    pygame.draw.rect(
        screen,
        (50, 50, 50),
        (width / 2 - ROAD_W / 2, 0, ROAD_W, height)
    )

    pygame.draw.rect(
        screen,
        (255, 240, 60),
        (width / 2 - ROADMARD_W / 2, 0, ROADMARD_W, height)
    )

    pygame.draw.rect(
        screen,
        (255, 255, 255),
        (width / 2 - ROAD_W / 2 + ROADMARD_W * 2, 0, ROADMARD_W, height)
    )

    pygame.draw.rect(
        screen,
        (255, 255, 255),
        (width / 2 + ROAD_W / 2 - ROADMARD_W * 3, 0, ROADMARD_W, height)
    )

    screen.blit(car, car_loc)
    screen.blit(car_two, car_two_loc)
    pygame.display.update()

pygame.quit()