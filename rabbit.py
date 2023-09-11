from random import randint

class Rabbit():
    def __init__(self, move_range):
        self.move_range = move_range
        print('new rabbit')

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