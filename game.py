import rabbit
from random import randint

startingPosition = randint(0, 99)
guess = 0

class Game():
    def __init__(self, gameSize):
        self.gameSize = gameSize
        self.guess = guess
        self.rabbit = rabbit.Rabbit(gameSize)
        self.rabbit.setPosition(startingPosition)
        print('rabbit started at position ', startingPosition)

        self.rabbitFound = False


    def update(self):

        if not self.rabbitFound:
            if self.makeGuess():
                self.rabbitFound = False

        self.rabbit.move()

    def makeGuess(self):
        self.guess += 1   

        if self.guess > self.gameSize:
            self.guess = 0
        
        print('guessing position: ', self.guess)

        if self.guess == self.rabbit.position:
            print('found rabbit at position ', self.rabbit.position)
            self.rabbitFound = True
