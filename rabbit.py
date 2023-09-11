from random import randint
from pygame import *

class Rabbit():
    def __init__(self, move_range, window):
        self.window = window
        self.height = 10
        self.width = 10
        self.icon = Surface((self.width, self.height))
        self.move_range = move_range
        print('new rabbit')
        
        self.icon.fill('black')

    def setPosition(self, pos):
        self.position = pos
        print('set rabbit position to: ', self.position)

    def move(self):
        move = randint(0,1)

        if move == 1:
            self.position += 1
            print('rabit moved right (', self.position, ')')

        else:
            self.position -= 1
            print('rabit moved left (', self.position, ')')

        if self.position > self.move_range:
            self.position -= 2

        elif self.position < 0:
            self.position += 2

    def draw(self):
        self.window.blit(self.icon, (self.position * 10, 300))