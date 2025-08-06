from code import entity
from code.enemy import Enemy
from code.entity import Entity


class EntityMediator:
    @staticmethod
    def __collision_window_check(ent: Entity):
        if isinstance(ent, Enemy):
            if ent.rect.right < 0:
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

