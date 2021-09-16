from nlc_dino_runner.componentes.obstacles.cactus import Cactus
from nlc_dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS
import random

class ObstaclesManager:

    def __init__(self):
        self.obstacles_list = []

    def update(self, game):
        size_cactus = random.randint(1, 2)
        if len(self.obstacles_list) == 0:
            if size_cactus == 1:
                self.obstacles_list.append(Cactus(SMALL_CACTUS))
            elif size_cactus == 2:
                self.obstacles_list.append(Cactus(LARGE_CACTUS))

        for obstacle in self.obstacles_list:
            obstacle.update(game.game_speed, self.obstacles_list)
            if game.player.dino_rect.colliderect(obstacle.rect):
                game.playing = False
                game.death_count += 1
                break

    def draw(self, screen):
        for obstacle in self.obstacles_list:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles_list =[]
