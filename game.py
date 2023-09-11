import rabbit
from random import randint

startingPosition = randint(0, 99)
guess = 0

class Game():
    def __init__(self, gameSize):
        # start new game with rabit at random position
        self.gameSize = gameSize
        self.rabbit = rabbit.Rabbit(gameSize)
        self.rabbit.setPosition(startingPosition)
        print('rabbit started at position ', startingPosition)

        # init game variables
        self.rabbitFound = False
        self.guess = guess

    # guess which position rabbit is at
    def makeGuess(self):

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

        if not self.rabbitFound:
            if self.makeGuess():
                self.rabbitFound = False

        self.rabbit.move()

