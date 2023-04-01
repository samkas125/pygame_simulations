import pygame
import math
from pygame.locals import *
import os
import time

# Input time period and amplitude
n = 0
while n < 2:
    m = float(input('Enter the mass of oscillating object of the mass-spring system (in kg - use values from 1 to 10 for best results): '))
    if m > 0:
        n += 1
    else:
        print("Invalid value for mass. Please enter again")
        n = 0
        continue
    amplitude = float(input("Enter the amplitude of the mass-spring system in pixels (0 to 450): "))
    if amplitude >= -450 and amplitude <= 450:
        n += 1
    else:
        print("Invalid value for amplitude. Please enter again")
        n = 0
        continue
print("Please check the opened pygame window to view the simulation. Press 'space' to start it.")
T = 2 * math.pi * math.sqrt(m / 10)
#INITIALIZATION OF PYGAME OBJECTS
pygame.init()
WINDOW = pygame.display.set_mode((900, 600))
pygame.display.set_caption('Pendulum simulation')
FPS = 30
BOB_OBJ = pygame.image.load(os.path.join('assets', 'soccerball.png'))
font = pygame.font.Font(os.path.join('fonts', 'font.ttf'), 24)
text_color = (255, 255, 255)
OX = 450
OY = 300
ORIGIN = (OX, OY)
PI = math.pi
omega = (2 * math.pi) / T
# Initializing displacement function for SHM
def displacement(time):
    return amplitude * math.cos(omega * time)

def velocity(time):
    return -1 * amplitude * omega * math.sin(omega * time)

def acceleration(time):
    return -1 * amplitude * omega * omega * math.cos(omega * time)

#DRAWS THE SIMULATION ON THE WINDOW
def draw_window(time):
    WINDOW.fill((0, 0, 0))
    curr_displacement = displacement(time)
    pygame.draw.line(WINDOW, (255, 255, 255), (0, OY + 12), (OX + curr_displacement + 12, OY + 12))
    WINDOW.blit(BOB_OBJ, (OX + curr_displacement, OY))
    disp_text = font.render(f'Displacement: {int(curr_displacement)} px', True, text_color)
    vel_text = font.render(f'Velocity: {int(velocity(time))} px / s', True, text_color)
    accel_text = font.render(f'Acceleration: {int(acceleration(time))} px / s^2', True, text_color)
    WINDOW.blit(accel_text, (100, 150))
    WINDOW.blit(vel_text, (100, 100))
    WINDOW.blit(disp_text, (100, 50))
    pygame.display.update()
def main():
    clock = pygame.time.Clock()
    started = False
    run = True
    curr_time = 0
    draw_window(curr_time)
    
    while run:
        clock.tick(FPS)
        if not started: draw_window(curr_time)
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[K_SPACE] and not started:
            started = True
            curr_time = time.time()

        if started:
            time_diff = time.time() - curr_time
            draw_window(time_diff)

        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                run = False
                print('Simulation closed!')

main()
pygame.quit()