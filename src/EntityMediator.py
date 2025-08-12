from src.Const import WIN_WIDTH
from src.EnemyShot import EnemyShot
from src.PlayerShot import PlayerShot
from src.enemy import Enemy
from src.entity import Entity


class EntityMediator:
    @staticmethod
    def __collision_window_check(ent: Entity):
        if isinstance(ent, Enemy):
            if ent.rect.right <= 0:
                ent.health = 0
        if isinstance(ent, PlayerShot):
            if ent.rect.left >= WIN_WIDTH:
                ent.health = 0
        if isinstance(ent, EnemyShot):
            if ent.rect.right <= 0:
                ent.health = 0

    @staticmethod
    def collision_check(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            test_entity = entity_list[i]
            EntityMediator.__collision_window_check(test_entity)

    @staticmethod
    def health_check(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                entity_list.remove(ent)

