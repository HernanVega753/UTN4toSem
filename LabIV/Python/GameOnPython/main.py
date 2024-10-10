# Ejemplo de pantalla pygame
import pygame as pg

# Configuaración de pygame
pg.init()
screen = pg.display.set_mode((800, 600))
clock = pg.time.Clock()
running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

screen.fill('purple')

pg.display.flip()
clock.tick(60)

pg.quit()
