import pygame
from pygame.locals import *
import os

pygame.init()

# INPUT
n = True
while n:
    co_res = float(input('Enter coefficient of restitution (between 0 and 1): '))
    if co_res < 1 and co_res > 0:
        co_res *= -1 # FLIPPING THE DIRECTION OF THE VELOCITY AFTER THE BOUNCE
        n = False
        print('Coefficient of restitution is set! Check the new window that opened to view the simulation!')
    else:
        print("Invalid value of coefficient of restitution. Please enter again.")

#INITIALIZATION 
WINDOW = pygame.display.set_mode((900, 600))
pygame.display.set_caption('Bouncing ball simulation with coefficient of restitution')
FPS = 60
BALL_OBJ = pygame.image.load(os.path.join('assets', 'soccerball.png'))
font = pygame.font.Font(os.path.join('fonts', 'font.ttf'), 24)
text_color = (255, 255, 255)


#DRAWS THE SIMULATION ON THE PYGAME WINDOW. REPEATEDLY GETS CALLED   
def draw_window(rect, hMax, font, text_color, co_res):
        WINDOW.fill((0, 0, 0))
        pygame.draw.line(WINDOW, (255, 255, 255), (100, 524), (800, 524))
        pygame.draw.line(WINDOW, (255, 255, 255), (100, 525), (800, 525))
        WINDOW.blit(BALL_OBJ, (rect.x, rect.y))
        bounceHeight = font.render(f'Height of bounce: {500 - hMax} px', True, text_color)
        coRest = font.render(f'Coefficient of restitution: {co_res * -1}', True, text_color)
        WINDOW.blit(bounceHeight, (100, 100))
        WINDOW.blit(coRest, (100, 200))
        pygame.display.update()

#MAIN FUNCTION THAT RUNS THE SIMULATION
def main(co_res):
    clock = pygame.time.Clock()
    started = False
    run = True
    hMax = 100
    ball_rect = pygame.Rect(450, 100, 24, 24)
    y_change = 0
   
    draw_window(ball_rect, hMax, font, text_color, co_res)
    while run:
        clock.tick(FPS) # CONTINUOUS LOOP - TICK FUNCTION MAKES IT RUN 60 TIMES A SECOND
        draw_window(ball_rect, hMax, font, text_color, co_res)
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[K_SPACE]:
            started = True
        
        
        if started:
            y_change += 0.3 #INCREASING VELOCITY OF THE BALL - ACCELERATION
            ball_rect.y += y_change
            draw_window(ball_rect, hMax, font, text_color, co_res)
     
        if y_change < 0.15 and y_change >= -0.15 and started: # CHECKS IF BALL IS AT MAX HEIGHT
            print(f'Max height of bounce: {500 - ball_rect.y} px')
            hMax = ball_rect.y
            if (500-hMax) <= 20:
                started = False
                ball_rect.y = 500
                draw_window(ball_rect, hMax, font, text_color, co_res)

        
        

        if ball_rect.y >= 500 and y_change > 0: # CHECKS IF THE BALL HAS HIT THE BOTTOM, AND IF IT IS GOING DOWNWARDS
            y_change = co_res * y_change

        for event in pygame.event.get(): # ALLOWS USER TO CLOSE THE PYGAME WINDOW
            if event.type == pygame.QUIT:
                run = False
        
        
main(co_res)

pygame.quit()
    
 