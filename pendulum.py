import pygame
import math
from pygame.locals import *
import os


# theta = 70
# length = 400
n = 0
while n < 2:
    theta = float(input('Enter the initial angle of displacement of the pendulum (90 to 0) : '))
    if theta <= 90 and theta >= 0:
        n += 1
    else:
        print("Invalid value for angle of displacement. Please enter again")
        continue
    length = int(input("Enter the length of the pendulum in pixels (10 to 500): "))
    if length <= 500 and length >= 10:
        n += 1
    else:
        print("Invalid value for length of pendulum. Please enter again")
        continue

print("Please check the opened pygame window to view the simulation. Press 'space' to start it.")


pygame.init()

WINDOW = pygame.display.set_mode((900, 600))
pygame.display.set_caption('Pendulum simulation')
FPS = 200
BOB_OBJ = pygame.image.load(os.path.join('assets', 'soccerball.png'))
font = pygame.font.Font(os.path.join('fonts', 'font.ttf'), 24)
text_color = (255, 255, 255)
OX = 450
OY = 50
ORIGIN = (OX, OY)
G = 9.8 * 100

def draw_window(rad, vel, accel):
    WINDOW.fill((0, 0, 0))
    dX = (length * math.sin(rad))
    dY = (length * math.cos(rad))
    pygame.draw.line(WINDOW, (255, 255, 255), (OX, OY), ((OX - dX), (OY + dY)))
    pygame.draw.line(WINDOW, (255, 255, 255), (200, OY), (700, OY))
    pygame.draw.line(WINDOW, (255, 0, 0), (OX, OY), (OX, 500))
    velocity = font.render(f'Velocity: {int(vel)} px / s', True, text_color)
    angle = font.render(f'Angle: {int((rad/math.pi) * 180)} degrees', True, text_color)
    acceleration = font.render(f'Tangential acceleration: {int(accel)} px / s^2', True, text_color)
    WINDOW.blit(velocity, (100, 300))
    WINDOW.blit(angle, (100, 400))
    WINDOW.blit(acceleration, (100, 500))
    # timeP = font.render(f'Height of bounce: {500 - hMax} px', True, text_color)

    WINDOW.blit(BOB_OBJ, (OX - dX - 12, OY + dY - 12))
    pygame.display.update()

def newRad(rad, u):
    # using v = u + at
    a = G * math.sin(rad)
    t = 1/FPS
    v = u + a * t

    # Using s = ut + (0.5)at^2
    arcLen = v * t + 0.5 * a * t * t
    # Using arclen = radian * radius
    dRad = arcLen / length
    newRad = rad - dRad
    return [newRad, v, a]


def main():

    radian = (theta/180) * math.pi
    vel = 0
    accel = 0
    clock = pygame.time.Clock()
    started = False
    run = True
    draw_window(radian, vel, accel)
    while run:
        clock.tick(FPS)
        draw_window(radian, vel, accel)
        

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[K_SPACE]:
            started = True

        if started:
            radvel = newRad(radian, vel)
            radian = radvel[0]
            vel = radvel[1]
            accel = radvel[2]
            draw_window(radian, vel, accel)

        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                run = False

main()
pygame.quit()