import pygame as pg
print('Setup Start')
pg.init()
screen = pg.display.set_mode(size=(800, 600))
print('Setup End')

print('Loop Start')
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit() #Close Game
            print('Game Closed')
            quit() #End Pygame