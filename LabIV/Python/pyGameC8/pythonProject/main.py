import sys
import random
import pygame
from sys import float_info
from personaje import Personaje, Enemigo
from explosiones import Explosion
from constantes import *

def mostrar_pantalla_inicio(screen):
    # Cargar y mostrar la imagen de inicio
    imagen_inicio = pygame.image.load(START_IMAGE_PATH)
    imagen_inicio = pygame.transform.scale(imagen_inicio, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(imagen_inicio, (0, 0))
    pygame.display.flip()

    # reproducir audio
    pygame.mixer.music.load(IMPERIAL_MARCH_PATH)
    pygame.mixer.music.play()

    # esperar que termine el audio
    while pygame.mixer.music.get_busy():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # actualizar pantalla
        screen.blit(imagen_inicio, (0, 0))
        pygame.display.flip()

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Amenaza Fantasma')

    # cargar los recursos del juego
    icon = pygame.image.load(f'{ASSETS_PATH}/images/fondo001.jpg')
    pygame.display.set_icon(icon)

    fondo = pygame.image.load(f'{ASSETS_PATH}/images/fondo3.jpg')
    fondo = pygame.transform.scale(fondo, (SCREEN_WIDTH, SCREEN_HEIGHT))

    estrella = pygame.image.load(ESTRELLA_PATH)
    estrella = pygame.transform.scale(estrella, (SCREEN_WIDTH, SCREEN_HEIGHT))

    fondo1 = pygame.image.load(FONDO1_PATH)
    fondo1 = pygame.transform.scale(fondo1, (SCREEN_WIDTH, SCREEN_HEIGHT))

    sonido_laser = pygame.mixer.Sound(f'{ASSETS_PATH}/sound/explosion.mp3')

    personaje = Personaje(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    enemigos = []
    explosiones = []
    puntos = 0
    nivel = 1

    clock = pygame.time.Clock()
    running = True

    # inicializar el fondo actual con el fondo original
    fondo_actual = fondo

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        dx, dy = 0, 0

        if keys[pygame.K_LEFT]:  # izquierda
            dx = -5
        if keys[pygame.K_RIGHT]:  # derecha
            dx = 5
        if keys[pygame.K_UP]:  # arriba
            dy = -5
        if keys[pygame.K_DOWN]:  # abajo
            dy = 5

        personaje.mover(dx, dy)

        if keys[pygame.K_SPACE]:
            personaje.lanzar_lasers()  # Corregido el método
            sonido_laser.play()

        for enemigo in enemigos:
            enemigo.mover()
            if enemigo.rect.top > SCREEN_HEIGHT:
                enemigos.remove(enemigo)  # Corregido el método de eliminación
            for laser in personaje.lasers:
                if enemigo.rect.colliderect(laser.rect):  # Usar rect de laser
                    explosiones.append(Explosion(enemigo.rect.centerx, enemigo.rect.centery))
                    enemigos.remove(enemigo)
                    personaje.lasers.remove(laser)
                    sonido_laser.play()  # Cambiar al sonido de explosión
                    puntos += 10
                    break
            if enemigo.rect.colliderect(personaje.shape):  # Usar shape de personaje
                if not personaje.definir_dano():  # Cambiado a definir_dano
                    running = False

        if random.random() < 0.02:
            x = random.randint(0, SCREEN_WIDTH - 50)
            enemigo = Enemigo(x, 0)
            enemigos.append(enemigo)  # Añadir el enemigo correctamente

        # Actualizar explosiones
        explosiones = [explosion for explosion in explosiones if explosion.actualizar()]

        # Cambiar fondo de pantalla según los puntos
        if puntos >= 250:
            if fondo_actual == fondo:
                fondo_actual = estrella
            else:
                fondo_actual = fondo1
                puntos = 0  # Cambiado para reiniciar puntos
                nivel += 1  # incrementa el nivel

        screen.blit(fondo_actual, (0, 0))
        personaje.dibujar(screen)
        for enemigo in enemigos:
            enemigo.dibujar(screen)
        for explosion in explosiones:
            explosion.dibujar(screen)

        # mostrar marcador y el nivel
        font = pygame.font.Font(None, 36)  # Corregido el método
        texto_puntos = font.render(f"Puntos: {puntos}", True, (255, 255, 255))
        texto_nivel = font.render(f'Nivel {nivel}', True, (255, 255, 255))  # Cambiado nivel1 a nivel

        screen.blit(texto_puntos, (10, 50))
        screen.blit(texto_nivel, (10, 90))

        pygame.display.flip()
        clock.tick(60)

    # mostrar mensaje de GAME OVER
    screen.fill((0, 0, 0))  # Cambiado a una tupla
    texto_game_over = font.render('GAME OVER', True, (255, 0, 0))  # Añadido True para el antialias
    texto_mensaje_final = font.render("QUE LA FUERZA TE ACOMPAÑE", True, (255, 255, 255))

    # mostrar frase
    screen.blit(texto_game_over, (SCREEN_WIDTH // 2 - texto_game_over.get_width() // 2, SCREEN_HEIGHT // 2 - 20))  # Corregido el cálculo de posición
    screen.blit(texto_mensaje_final, (SCREEN_WIDTH // 2 - texto_mensaje_final.get_width() // 2, SCREEN_HEIGHT // 2 + 20))

    pygame.display.flip()
    pygame.time.wait(2000)  # muestra la frase game over por 2 segundos

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
