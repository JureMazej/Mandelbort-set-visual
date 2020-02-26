from Mandelbrot import *
import pygame

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

pygame.init()

size = [400, 400]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Mandelbort set")
clock = pygame.time.Clock()

# ----------- Main --------------
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # On window closed
            done = True

    # LOGIC
    #
    #
    # #

    # DRAW
    for x in range(0, 400, 50):
        pygame.draw.ellipse(screen, red, [x, x, 25, 25], 0)
        x += 2

    pygame.display.flip()  # Update
    clock.tick(20)

pygame.quit()
