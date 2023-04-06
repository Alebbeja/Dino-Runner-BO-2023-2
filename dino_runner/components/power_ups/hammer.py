import random
import time
from dino_runner_components_obstacles_obstacle import Obstacle

class Hammer(Obstacle):
    def __init__(self):
        self.score = 0
        self.high_score = 0
        self.is_game_over = False
        self.is_jumping = False
        self.jump_height = 10
        self.hammer_pos = [100, 0]
        self.hammer_time = time.time() + 45
        self.cactus_pos = [150, 0]

    def jump(self):
        if not self.is_jumping:
            self.is_jumping = True

    def update(self):
        if self.is_jumping:
            self.jump_height -= 1
            if self.jump_height <= 0:
                self.is_jumping = False
                self.jump_height = 10

        if time.time() >= self.hammer_time:
            self.hammer_pos[0] = 100
            self.hammer_pos[1] = 0
            self.hammer_time = time.time() + 45  
        
        if self.hammer_pos[0] < -10:
            self.hammer_pos[0] = 100
            self.hammer_pos[1] = random.randint(10, 40)

        if self.cactus_pos[0] < -10:
            self.cactus_pos[0] = 150
            self.cactus_pos[1] = random.randint(10, 40)

        if self.hammer_pos[0] >= 50 and self.hammer_pos[0] <= 90 and self.hammer_pos[1] >= 0 and self.hammer_pos[1] <= 20:
            self.score += 10
            self.hammer_pos[0] = -100

        if self.cactus_pos[0] >= 50 and self.cactus_pos[0] <= 90 and self.cactus_pos[1] >= 0 and self.cactus_pos[1] <= 20:
            if self.hammer_pos[1] == 0:
                self.is_game_over = True
            else:
                self.score += 10
                self.cactus_pos[0] = -100 if self.hammer_pos[0] <-10
                self.hammer_pos[0] = 100
                self.hammer_pos[1] = random.randint(10, 40)

        if self.cactus_pos[0] < -10:
            self.cactus_pos[0] = 150
            self.cactus_pos[1] = random.randint(10, 40)

        if self.hammer_pos[0] >= 50 and self.hammer_pos[0] <= 90 and self.hammer_pos[1] >= 0 and self.hammer_pos[1] <= 20:
            self.score += 10
            self.hammer_pos[0] = -100

        if self.cactus_pos[0] >= 50 and self.cactus_pos[0] <= 90 and self.cactus_pos[1] >= 0 and self.cactus_pos[1] <= 20:
            if self.hammer_pos[1] == 0:
                self.is_game_over = True
            else:
                self.score += 10
                self.cactus_pos[0] = -100
