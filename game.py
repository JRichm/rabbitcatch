import rabbit
from ui_components import Scale
from random import randint
from pygame import *

startingPosition = randint(0, 99)
guess = 0


class Game():
    def __init__(self, gameSize, window):
        # start new game with rabit at random position
        self.window = window
        self.gameSize = gameSize
        self.ui_scale = Scale(window, gameSize)
        self.rabbit = rabbit.Rabbit(gameSize, window)
        self.rabbit.setPosition(startingPosition)
        print('rabbit started at position ', startingPosition)

        # init game variables
        self.rabbitFound = False
        self.guess = guess

        # create guess square icon
        self.guess_icon = Surface((10,10))
        self.guess_icon.fill('green')

    # guess which position rabbit is at
    def makeGuess(self):

        # update guess
        self.guess += 1   
        if self.guess > self.gameSize:
            self.guess = 0
        
        print('guessing position: ', self.guess)
        self.window.blit(self.guess_icon, (self.guess * 10, 320))

        # check guess
        if self.guess == self.rabbit.position:
            print('found rabbit at position ', self.rabbit.position)

            #stop loop if rabbit found
            self.rabbitFound = True            

    # update gets called every frame from main
    def update(self):

        # make guess if rabbit is not found
        if not self.rabbitFound:
            if self.makeGuess():
                self.rabbitFound = False
            
            else:
                # move rabbit after guess
                self.rabbit.move()

        self.rabbit.draw()
        self.ui_scale.draw()

