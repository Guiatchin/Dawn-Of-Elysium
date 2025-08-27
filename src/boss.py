from src.Const import ENTITY_SPEED
from src.enemy import Enemy

class Boss(Enemy):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self, ):
        self.rect.centerx -= ENTITY_SPEED[self.name]

    def shoot(self):
        pass