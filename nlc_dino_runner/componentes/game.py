import pygame


from nlc_dino_runner.utils.constants import Title, ICON, SCREEN_WIDTH, SCREEN_HEIGHT, BG, FPS

class Game:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption(Title)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.x_pos_bg = 0
        self.y_pos_bg = 360
        self.playing = False
        self.game_speed = 20
        self.clock = pygame.time.Clock()


    def run (self):
        self.playing = True
        print("JUGAR ")
        while self.playing:
            self.event()
            self.update()
            self.draw()

        pygame.quit()

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
        print("DETECTANDO EVENTO ")


    def update(self):
        pass


    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255,255,255))
        self.draw_bakground()
        pygame.display.update()
        pygame.display.flip()


    def draw_bakground(self):
        image_width= BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (self.x_pos_bg + image_width, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (self.x_pos_bg + image_width, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed