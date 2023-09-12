import rabbit
from ui_components import Scale
from random import randint
from pygame import *

class Game():
    def __init__(self, gameSize, window):
        # start new game with rabit at random position
        self.window = window
        self.gameSize = gameSize
        self.ui_scale = Scale(window, gameSize)
        self.rabbit = rabbit.Rabbit(gameSize, window)
        self.rabbit.setPosition(randint(0, gameSize))
        print('rabbit started at position ', self.rabbit.position)

        # init game variables
        self.rabbitFound = False
        self.guess = 0
        self.rabbitsTurn = False

        # create guess square icon
        self.guess_icon = Surface((10,10))
        self.guess_icon.fill('green')

    # guess which position rabbit is at
    def makeGuess(self):
        
        self.window.blit(self.guess_icon, (self.guess * 10, 315))

        # update guess
        self.guess += 1   
        if self.guess > self.gameSize:
            self.guess = 0
        
        print('guessing position: ', self.guess)

        # check guess
        if self.guess == self.rabbit.position:
            print('found rabbit at position ', self.rabbit.position)

            #stop loop if rabbit found
            self.rabbitFound = True            

    # update gets called every frame from main
    def update(self):

        self.rabbit.draw()

        if not self.rabbitFound:
            if self.rabbitsTurn:
                self.rabbit.move()
                self.rabbitsTurn = False


            else:
                if self.makeGuess():
                    self.rabbitFound = True

                self.rabbitsTurn = True

        
        self.ui_scale.draw()

