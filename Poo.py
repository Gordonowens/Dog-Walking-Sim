from BasicSprite import *

class Poo(BasicSprite):

    def __init__(self):


        BasicSprite.__init__(self, 0, 0, 30)
        self.image = pygame.transform.scale(
            self.createSprite(pygame.image.load('img/terrain2.png').convert(), 919, 325, 18, 18, (255, 255, 255)),
            (20, 20))
        self._layer = 1
