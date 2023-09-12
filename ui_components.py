from pygame import *

class Scale():
    def __init__(self, window, gameScale):
        self.window = window
        scale_part = Surface((10, 4))
        scale_part.fill('black')
        scale_part.fill('white', Rect(1, 1, 8, 9))
        self.scaleIcon = Surface((gameScale * 10, 5))

        for x in range(gameScale):
            self.scaleIcon.blit(scale_part, (x * 10, 0))



    def draw(self):
        self.window.blit(self.scaleIcon, (0, 310))