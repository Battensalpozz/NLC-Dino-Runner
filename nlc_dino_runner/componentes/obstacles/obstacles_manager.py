import pygame

from nlc_dino_runner.componentes.obstacles.cactus import Cactus
from nlc_dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, DINO_DEAD, SOUND_COLLISION, \
    SOUND_HAMMER_COLLISION

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
            if game.power_up_manager.hammer.rect.colliderect(obstacle.rect):
                if obstacle in self.obstacles_list:
                    SOUND_HAMMER_COLLISION.play()
                    self.obstacles_list.remove(obstacle)

            if game.player.dino_rect.colliderect(obstacle.rect):
                if game.player.shield:
                    self.obstacles_list.remove(obstacle)
                elif game.life_manager.life_counter() == 1:
                    game.life_manager.delete_life()
                    game.player.image = DINO_DEAD
                    game.death()
                    pygame.time.delay(1500)
                    game.playing = False
                    game.death_count += 1
                    break
                else:
                    game.life_manager.delete_life()
                    SOUND_COLLISION.play()
                    if obstacle in self.obstacles_list:
                        self.obstacles_list.remove(obstacle)


    def draw(self, screen):
        for obstacle in self.obstacles_list:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles_list = []
