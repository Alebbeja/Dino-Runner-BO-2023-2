import pygame

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS
from dino_runner.components import text_utils
from dino_runner.components import dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager 

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = False
        self.playing = False
        self.game_speed = 20
        self.cloud_speed= 2
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_manager = PowerUpManager()
        self.points = 0

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
                pygame.quit()
            if event.type == pygame.KEYDOWN and not self.playing:
                self.playing = True

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self.game_speed, self.player)
        self.power_up_manager.update(self.game_speed, self.points, self.player)
        self.point += 1
        if self.player.dino_dead:
            self.playing = False

    def draw(self):
        if self.playing:
           self.clock.tick(FPS)
           self.screen.fill((255, 255, 255))
           self.draw_background()
           self.player.draw(self.screen)
           self.obstacle_manager.draw(self.screen)
           self.draw_score()
           self.power_up_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def draw_score(self):
        score, score_rect = text_utils.get_message('points' + self.points, 20, 1000, 40)
        self.screen.blit(score, score_rect)

    def draw_menu(self):
        white_color = (255, 255, 255)
        self.screen.fill(white_color)
        self.print_menu_element()

    def print_menu_element():
        if self.death_count == 0:
           text, text_rect = text_utils.get_message('press any key to star', 30)
           self.screen.blit(text, text_rect)
        else:
           text, text_rect = text_utils.get_message('press any key to star', 30)
           score, score_rect = text_utils.get_message('your score: ' + str(self))
           self.screen.blit(text, text_rect)
           
