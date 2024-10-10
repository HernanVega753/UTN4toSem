import pygame as pg

# Configuración de la pantalla
screen = pg.display.set_mode((800, 600))
clock = pg.time.Clock()
running = True
delta = 0

# Posición de pantalla
player_pos = pg.Vector2(screen.get_width() / 2, screen.get_height() / 2)

# Velocidad del jugador
speed = 5

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Detectar teclas para presionar
    keys = pg.key.get_pressed()

    # Movimiento del jugador
    if keys[pg.K_LEFT]:  # Tecla izquierda
        player_pos.x -= speed
    if keys[pg.K_RIGHT]:  # Tecla izquierda
        player_pos.x += speed
    if keys[pg.K_DOWN]:  # Tecla izquierda
        player_pos.y += speed
    if keys[pg.K_UP]:  # Tecla izquierda
        player_pos.y -= speed
    # Limpiar pantalla
    screen.fill('green')

    # Dibujar el jugador (en este caso un círculo rojo)
    pg.draw.circle(screen, (255, 0, 0), (int(player_pos.x), int(player_pos.y)), 10)

    # Actualizar pantalla
    pg.display.flip()

    # Control de velocidad del jugador FPS
    clock.tick(60)

pg.quit()  # Cierre de pantalla
