import pygame
import game


# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
running = True
keys = []

newGame = game.Game(100)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE
    newGame.update()

    if newGame.rabbitFound:
        running = False

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limit FPS to 60
    clock.tick(60)

pygame.quit()