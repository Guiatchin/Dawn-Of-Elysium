from code.Const import WIN_WIDTH
from code.background import Background


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str,position=(0,0)):
        match entity_name:
            case 'bg30':
                list_bg = []
                for i in range(5):
                    list_bg.append(Background(f'bg3{i}', (0,0)))
                    list_bg.append(Background(f'bg3{i}', (WIN_WIDTH,0)))
                return list_bg





