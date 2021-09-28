import random

from nlc_dino_runner.componentes.obstacles.obstacles import Obstacles



class Bird(Obstacles):

    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 267
        self.index = 0

    def draw(self, screen):
        if self.index >= 10 :
            self.index = 0
        screen.blit(self.image[self.index//5], self.rect)
        self.index += 1