import pygame
from pygame import draw, display

# Initialize Pygame
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Dragon.....')

# Define rectangles for dragon parts
tail = pygame.Rect(50, 150, 80, 25)
backLeg = pygame.Rect(140, 150, 35, 150)
tummy = pygame.Rect(185, 150, 35, 100)
frontLeg = pygame.Rect(230, 150, 35, 150)
neck = pygame.Rect(275, 140, 40, 55)
head = pygame.Rect(325, 120, 55, 50)
nose = pygame.Rect(370, 130, 40, 40)
eye1 = pygame.Rect(330, 130, 8, 8)
eye2 = pygame.Rect(360, 130, 8, 8)


# Define a function to move the dragon
def move_dragon(dx, dy):
    tail.move_ip(dx, dy)
    backLeg.move_ip(dx, dy)
    tummy.move_ip(dx, dy)
    frontLeg.move_ip(dx, dy)
    neck.move_ip(dx, dy)
    head.move_ip(dx, dy)
    nose.move_ip(dx, dy)
    eye1.move_ip(dx, dy)
    eye2.move_ip(dx, dy)


# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                move_dragon(0, -10)
            elif event.key == pygame.K_DOWN:
                move_dragon(0, 10)
            elif event.key == pygame.K_LEFT:
                move_dragon(-10, 0)
            elif event.key == pygame.K_RIGHT:
                move_dragon(10, 0)
            #elif event.key == pygame.K_SPACE:
            #    move_dragon((random.randint(0, 200)), (random.randint(0, 200)))
    # Clear screen
    screen.fill("violet")

    # Draw dragon parts
    draw.rect(screen, "green", tail)
    draw.rect(screen, "green", backLeg)
    draw.rect(screen, "green", tummy)
    draw.rect(screen, "green", frontLeg)
    draw.rect(screen, "green", neck)
    draw.rect(screen, "green", head)
    draw.rect(screen, "green", nose)
    draw.rect(screen, "black", eye1)
    draw.rect(screen, "black", eye2)

    # Update display
    display.update()

# Ensure the event loop ends before closing
pygame.quit()

# Note: Uncomment the call to the function to test and run in your environment
# This file should be tested in a proper Python environment with Pygame installed
