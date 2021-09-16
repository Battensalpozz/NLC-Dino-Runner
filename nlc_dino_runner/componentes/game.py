import pygame
import os

from nlc_dino_runner.componentes.obstacles.obstacles_manager import ObstaclesManager
from nlc_dino_runner.utils import text_utils
from nlc_dino_runner.utils.constants import Title, ICON, SCREEN_WIDTH, SCREEN_HEIGHT, BG, FPS
from nlc_dino_runner.componentes.Dinosaurio import Dinosaur



class Game:

    def __init__(self):
        IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")
        icono = pygame.image.load(os.path.join(IMG_DIR, "DinoWallpaper.png"))
        pygame.init()
        pygame.display.set_caption(Title)
        pygame.display.set_icon(icono)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.x_pos_bg = 0
        self.y_pos_bg = 360
        self.playing = False
        self.game_speed = 20
        self.clock = pygame.time.Clock()
        self.player = Dinosaur()
        self.obstacle_manager = ObstaclesManager()
        self.points = 0
        self.running = True
        self.death_count = 0

    def run (self):
        self.obstacle_manager.reset_obstacles()
        self.points = 0
        self.playing = True
        while self.playing:
            self.event()
            self.update()
            self.draw()


    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False



    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)


    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255,255,255))
        self.score()
        self.draw_bakground()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def score(self):
        self.points += 1

        if self.points % 1000 ==0:
            self.game_speed += 1
        score_element, score_element_rect = text_utils.get_score_element(self.points)
        self.screen.blit(score_element, score_element_rect)


    def draw_bakground(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (self.x_pos_bg + image_width, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (self.x_pos_bg + image_width, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def execute (self):
        while self.running:
            if not self.playing:
                self.show_menu()

    def show_menu(self):
        self.running = True
        white_color = (255, 255, 255)
        self.screen.fill(white_color)
        self.print_menu_elements()
        pygame.display.update()
        self.handle_key_events_on_menu()


    def handle_key_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
                pygame.display.quit()
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                self.run()

    def print_menu_elements(self):
        half_screen_height = SCREEN_HEIGHT // 2
        if self.death_count > 0:
            text, text_rect = text_utils.get_centered_masage("Press any Key to Restart ")
            self.screen.blit(text, text_rect)
            last_score, last_score_rect = text_utils.get_centered_masage("Last Score: " + str(self.points), height= half_screen_height + 100)
            self.screen.blit(last_score, last_score_rect)
        else:
            text, text_rect = text_utils.get_centered_masage("Press any Key to Start ")
            self.screen.blit(text, text_rect)

        death_score, death_score_rect = text_utils.get_centered_masage("Dead Count: " + str(self.death_count), height= half_screen_height +50)
        self.screen.blit(death_score, death_score_rect)
        self.screen.blit(ICON, ((SCREEN_WIDTH // 2) - 40, (SCREEN_HEIGHT // 2) - 150))





