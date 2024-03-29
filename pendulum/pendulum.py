import pygame
import math
from pygame.locals import *
import os

#INPUTTING VALUES OF ANGLE AND LENGTH
theta = 70
length = 400.0
n = 0
while n < 2:
    theta = float(input('Enter the initial angle of displacement of the pendulum (90 to 0) : '))
    if theta <= 180 and theta >= 0:
        n += 1
    else:
        print("Invalid value for angle of displacement. Please enter again")
        n = 0
        continue
    length = float(input("Enter the length of the pendulum in pixels (10 to 500): "))
    if length <= 500 and length >= 10:
        n += 1
    else:
        print("Invalid value for length of pendulum. Please enter again")
        n = 0
        continue

print("Please check the opened pygame window to view the simulation. Press 'space' to start it.")

#INITIALIZATION OF PYGAME OBJECTS
pygame.init()

WINDOW = pygame.display.set_mode((900, 600))
pygame.display.set_caption('Pendulum simulation')
FPS = 30
BOB_OBJ = pygame.image.load(os.path.join('assets', 'soccerball.png'))
font = pygame.font.Font(os.path.join('fonts', 'font.ttf'), 24)
text_color = (255, 255, 255)
OX = 450
OY = 50
ORIGIN = (OX, OY)
G = 500.1
PI = math.pi

#DRAWS THE SIMULATION ON THE WINDOW
def draw_window(rad, vel, accel):
    WINDOW.fill((0, 0, 0))
    dX = (length * math.sin(rad))
    dY = (length * math.cos(rad))
    pygame.draw.line(WINDOW, (255, 255, 255), (OX, OY), ((OX - dX), (OY + dY)))
    pygame.draw.line(WINDOW, (255, 255, 255), (200, OY), (700, OY))
    pygame.draw.line(WINDOW, (255, 0, 0), (OX, OY), (OX, OY + length))
    velocity = font.render(f'Velocity: {int(vel)} px / s', True, text_color)
    angle = font.render(f'Angle: {int((rad/math.pi) * 180)} degrees', True, text_color)
    acceleration = font.render(f'Tangential acceleration: {int(accel)} px / s^2', True, text_color)
    timeP_form = font.render(f'Time period: {round((2 * math.pi) * math.sqrt(float(length)/float(G)), 2)} s', True, text_color)
    WINDOW.blit(timeP_form, (100, 200))
    WINDOW.blit(velocity, (100, 300))
    WINDOW.blit(angle, (100, 400))
    WINDOW.blit(acceleration, (100, 500))
    # timeP = font.render(f'Height of bounce: {500 - hMax} px', True, text_color)

    WINDOW.blit(BOB_OBJ, (OX - dX - 12, OY + dY - 12))
    pygame.display.update()
#CALCULATES NEW ANGLE BASED ON CURRENT ANGLE AND VELOCITY USING 4 FORMULAE
def newRad(rad, u):
    # using v = u + at
    a = G * math.sin(rad) # USING THE DERIVED FORMULA A = G*SIN(THETA) FOR PENDULUM
    t = 1/FPS
    v = u + a * t

    # Using s = ut + (0.5)at^2
    arcLen = v * t + 0.5 * a * t * t
    # Using arclen = radian * radius
    dRad = arcLen / length
    newRad = rad - dRad
    return [newRad, v, a] # RETURNS THE NEW ANGLE, VELOCITY AND ACCELERATION


def main():

    #INITIALIZATION OF ANGLE, VELOCITY AND ACCELERATION
    radian = (theta/180) * math.pi
    vel = 0
    accel = G * math.sin(radian)
    clock = pygame.time.Clock()
    started = False
    run = True
    # time_f = 0
    draw_window(radian, vel, accel)
    
    while run:
        clock.tick(FPS)
        draw_window(radian, vel, accel)
        

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[K_SPACE]:
            started = True
            # time_init = pygame.time.get_ticks()

        if started:
            radvel = newRad(radian, vel)
            radian = radvel[0]
            vel = radvel[1]
            accel = radvel[2]
            draw_window(radian, vel, accel)

        # if started and vel < 5 and vel > -5 and radian > 0: # checking that the velocity is approximately zero, and that the ball is at the left side peak
        #     time_f = pygame.time.get_ticks()
        #     time_period = time_f - time_init
        #     time_init = time_f
        #     print(time_period)

        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                run = False
                print('Simulation closed!')

main()
pygame.quit()