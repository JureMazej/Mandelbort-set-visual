from Mandelbrot import Mandelbrot
import pygame


def map_pixel(value, start1, end1, start2, end2):
    return start2 + (end2 - start2) * ((value - start1) / (end1 - start1))


# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

pygame.init()

windowX = 400
windowY = 400

size = [windowX, windowY]

screen = pygame.display.set_mode(size)

pygame.display.set_caption("Mandelbort set")
clock = pygame.time.Clock()

# ----------- Main --------------
done = False
while not done:

    # EVENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # On window closed
            done = True

    # LOGIC
    #
    #
    # #

    # DRAW
    for x in range(0, windowX, 1):
        for y in range(0, windowY, 1):
            x0 = map_pixel(x, 0, windowX, -2, 2)
            y0 = map_pixel(y, 0, windowX, -2, 2)
            m = Mandelbrot(windowX, windowY)
            if m.mandel_eq(x0, y0):
                screen.set_at((x, y), blue)
            else:
                screen.set_at((x, y), red)

    pygame.display.flip()  # Update
    clock.tick(1)

pygame.quit()
