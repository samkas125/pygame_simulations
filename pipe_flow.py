from pygame.locals import *
import math, os, pygame

pygame.init()

# input user values of radius and viscosity
n = 0
while n < 2:
    radius = int(input('Enter the radius of the pipe in px: '))
    if radius >= 1:
        n += 1
    else:
        print("Invalid value for radius. Please enter again")
        continue
    viscosity = float(input("Enter the viscosity of the fluid in Pa*s: "))
    if viscosity >= 0:
        n += 1
    else:
        print("Invalid value for viscosity. Please enter again")
        continue

# Set values - not taken from user (pressure difference and length of pipe)
pressure_diff = 50
length = 700

WINDOW = pygame.display.set_mode((900, 600))
pygame.display.set_caption('Simulating the speed of fluid in a pipe')
FPS = 60
DROPLET = pygame.image.load(os.path.join('assets', 'drop.png'))
FONT = pygame.font.Font(os.path.join('fonts', 'font.ttf'), 24)
WHITE = (255, 255, 255)
BLUE = (0, 100, 100)
VEL = round((((pressure_diff * radius ** 2) / (8 * viscosity * length) ) / 60), 2)
# Use formula to calculate velocity of the ball in pixels / (1/60)th of a second
# Q = ΔPr^2 / 8ηl
print(VEL)

def draw_window(x_pos):
    pos = (x_pos + 100, 288 + 250)
    WINDOW.fill((0, 0, 0))
    #text
    rad = FONT.render(f'Radius of pipe = {radius} px', True, WHITE)
    vis = FONT.render(f'Viscosity of fluid = {viscosity} Pa*s', True, WHITE)
    leng = FONT.render(f'Length of pipe (preset) = {length} px', True, BLUE)
    pre = FONT.render(f'Pressure difference across 2 ends of the pipe (preset) = {pressure_diff} Pa', True, BLUE)
    vel = FONT.render(f'Velocity of fluid = {round(VEL * 60, 2)} px/s', True, WHITE)
    WINDOW.blit(rad, (70, 50))
    WINDOW.blit(vis, (70, 150))
    WINDOW.blit(leng, (70, 250))
    WINDOW.blit(pre, (70, 350))
    WINDOW.blit(vel, (70, 450))
    # lines and images
    pygame.draw.line(WINDOW, (255, 255, 255), (100, 288 + 250), (800, 288 + 250))
    pygame.draw.line(WINDOW, (255, 255, 255), (100, 312 + 250), (800, 312 + 250))
    WINDOW.blit(DROPLET, (pos))
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    started = False
    run = True
    x_pos = 0
    while run:
        clock.tick(FPS)
        draw_window(x_pos)

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[K_SPACE]:
            started = True
        
        if started:
            x_pos += VEL

        for event in pygame.event.get(): # ALLOWS USER TO CLOSE THE PYGAME WINDOW
            if event.type == pygame.QUIT:
                run = False
        if x_pos >= 700: # checks if the ball has reached the end of the pipe
            started = False

if __name__ == '__main__':
    main()


