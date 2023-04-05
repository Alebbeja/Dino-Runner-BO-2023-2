import pygame

class Bird:
    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 150
    GROUND_HEIGHT = 20
    GRAVITY = 0.6
    JUMP_VELOCITY = -10
    BIRD_WIDTH = 34
    BIRD_HEIGHT = 24
    BIRD_SPEED = 2
    FLAP_VELOCITY = -8
    BIRD_IMAGES = ["bird1.png", "bird2.png"]

    def __init__(self, x_pos):
        self.x_pos = x_pos
        self.y_pos = 50
        self.image = pygame.image.load("bird.png")
        self.rect = self.image.get_rect()
        self.rect.x = self.x_pos
        self.rect.y = self.y_pos

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        self.x_pos -= BIRD_SPEED
        self.rect.x = self.x_pos
        self.velocity += GRAVITY
        self.y_pos += self.velocity

    def collision(self, dino_rect):
        return self.rect.colliderect(dino_rect)
