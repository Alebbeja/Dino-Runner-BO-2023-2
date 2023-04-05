import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS
import random


class Cactus(Obstacle):
    Y_POS_CACTUS = 325
    
    def __init__(self):
        self.type = random.randint(0, 3)
        if self.type == 3:
            image = LARGE_CACTUS[random.randint(0, 2)]
        else:
            image = SMALL_CACTUS[self.type]
        super().__init__(image)
        self.rect.y = self.Y_POS_CACTUS
