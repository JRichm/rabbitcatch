import pygame
import game


# pygame setup
pygame.init()

gameWidth = 100

screen = pygame.display.set_mode((gameWidth*10, 600))
clock = pygame.time.Clock()
running = True
keys = []

newGame = game.Game(gameWidth, screen)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame

    # RENDER YOUR GAME HERE
    if not newGame.rabbitFound:
        screen.fill("white")
        newGame.update()

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limit FPS to 5
    clock.tick(60)

pygame.quit()