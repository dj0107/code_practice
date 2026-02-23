import pygame as pg
pg.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

size = [400, 300]
screen = pg.display.set_mode(size)
pg.display.set_caption("MY CHESSGAME")

done = False
clock = pg.time.Clock()

while not done:
    clock.tick(30)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
    
    screen.fill(WHITE)
    pg.draw.rect(screen, RED, [100, 100, 70, 30], 2)

    pg.display.flip()

pg.quit()