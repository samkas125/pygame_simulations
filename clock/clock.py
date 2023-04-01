import pygame, math, os
from pygame.locals import *

# Define the function to update the time variables
def update_time(time_str):
    global hour, minute, second
    hour, minute, second = map(int, time_str.split(':'))
    if not (hour <= 24 and hour >=0 and  minute >=0 and minute < 60 and second >= 0 and second < 60):
        raise Exception()

validated = False
while not validated:
    try:
        time_str = input("Enter the time (hh:mm:ss): ")
        update_time(time_str)
        validated = True
    except Exception as e:
        if e == 'KeyboardInterrupt':
            exit()
        print('Invalid values entered, try again.')

# Initialize Pygame
pygame.init()

# Define Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
TEXT_COLOR = (0, 65, 65)

# Set up the clock
clock = pygame.time.Clock()

# Set up the display
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600
WINDOW = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Analog Clock")
FPS = 15 # NOTE: Increasing FPS too much will reduce the accuracy of the clock due to additional latency

# Set up the font
font = pygame.font.Font(os.path.join('fonts', 'font.ttf'), 12)

# Define the center of the clock
center_x, center_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2

# Define the radius of the clock
clock_radius = 220

# Define the thickness of the clock hands
hour_hand_thickness = 10
minute_hand_thickness = 6
second_hand_thickness = 2

# Define the length of the clock hands
hour_hand_length = clock_radius * 0.5
minute_hand_length = clock_radius * 0.7
second_hand_length = clock_radius * 0.9

# Define the function to draw the clock face
def draw_clock_face():
    pygame.draw.circle(WINDOW, WHITE, (center_x, center_y), clock_radius)
    for i in range(12):
        if i == 0:
            clock_num = 12
        else:
            clock_num = i
        angle = math.radians(i * 30 - 90)
        x = center_x + clock_radius * math.cos(angle)
        y = center_y + clock_radius * math.sin(angle)
        pygame.draw.circle(WINDOW, GRAY, (int(x), int(y)), 10)
        clock_text = font.render(str(clock_num), True, TEXT_COLOR)
        WINDOW.blit(clock_text, (int(x)-6, int(y)-6))


# Define the function to draw a clock hand
def draw_hand(length, thickness, angle, color):
    x = center_x + length * math.cos(angle)
    y = center_y + length * math.sin(angle)
    pygame.draw.line(WINDOW, color, (center_x, center_y), (x, y), thickness)

# Define the main function
def main():
    global hour, minute, second

   
    # Start the game loop
    running = True
    started = False
    while running:

        clock.tick(FPS)

        keys_pressed = pygame.key.get_pressed() # Checking when spacebar is pressed
        if keys_pressed[K_SPACE]:
            started = True

        # Clear the screen
        WINDOW.fill(BLACK)

        # Draw the clock face
        draw_clock_face()

        # Calculate the angles of the clock hands
        hour_angle = math.radians((hour % 12) * 30 + minute / 2 - 90)
        minute_angle = math.radians(minute * 6 + second / 10 - 90)
        second_angle = math.radians(second * 6 - 90)

        # Draw the clock hands
        draw_hand(hour_hand_length, hour_hand_thickness, hour_angle, BLACK)
        draw_hand(minute_hand_length, minute_hand_thickness, minute_angle, BLACK)
        draw_hand(second_hand_length, second_hand_thickness, second_angle, BLACK)
        
        # Update the display
        pygame.display.update()
        if started:
            # Update the time variables
            second += 1/FPS
            if second == 60:
                second = 0
                minute += 1
            if minute == 60:
                minute = 0
                hour += 1
            if hour == 12:
                hour = 0

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    # Quit Pygame
    pygame.quit()
main()
