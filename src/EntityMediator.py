from src.Const import WIN_WIDTH
from src.EnemyShot import EnemyShot
from src.PlayerShot import PlayerShot
from src.enemy import Enemy
from src.entity import Entity
from src.player import Player


class EntityMediator:
    @staticmethod
    def __collision_window_check(ent: Entity):
        if isinstance(ent, Enemy):
            if ent.rect.right <= 0:
                ent.health = 0
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
    def __entity_collision_check(ent1, ent2):
        valid_collision = False
        if isinstance(ent1, Enemy) and isinstance(ent2, PlayerShot):
            valid_collision = True
        elif isinstance(ent1, Player) and isinstance(ent2, Enemy):
            valid_collision = True
        elif isinstance(ent1, PlayerShot) and isinstance(ent2, Enemy):
            valid_collision = True
        elif isinstance(ent1, Player) and isinstance(ent2, EnemyShot):
            valid_collision = True
        elif isinstance(ent1, EnemyShot) and isinstance(ent2, Player):
            valid_collision = True

        if valid_collision:
            if (ent1.rect.right >= ent2.rect.left and
                    ent1.rect.left <= ent2.rect.right and
                    ent1.rect.bottom >= ent2.rect.top and
                    ent1.rect.top <= ent2.rect.bottom):
                ent1.health -= ent2.damage
                ent2.health -= ent1.damage
                ent1.last_dmg = ent2.name
                ent2.last_dmg = ent1.name

    @staticmethod
    def __give_score(enemy: Enemy, entity_list: list[Entity]):
        if enemy.last_dmg == 'Player1Shot':
            for ent in entity_list:
                if ent.name == 'Player1':
                    ent.score += enemy.score
        elif enemy.last_dmg == 'Player2Shot':
            for ent in entity_list:
                if ent.name == 'Player2':
                    ent.score += enemy.score

    @staticmethod
    def collision_check(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.__collision_window_check(entity1)
            for j in range(i + 1, len(entity_list)):
                entity2 = entity_list[j]
                EntityMediator.__entity_collision_check(entity1, entity2)

    @staticmethod
    def health_check(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                if isinstance(ent, Enemy):
                    EntityMediator.__give_score(ent,entity_list)
                entity_list.remove(ent)
