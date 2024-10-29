import pygame
from constantes import ASSETS_PATH

class Personaje:
    def __init__(self, x, y):
        self.image = pygame.image.load(f'{ASSETS_PATH}/images/nave1.png')  # Corregido la ruta
        self.image = pygame.transform.scale(self.image, (95, 95))
        self.shape = self.image.get_rect(center=(x, y))
        self.lasers = []
        self.energia = 100  # Barra de vida

    def mover(self, dx, dy):
        self.shape.x += dx
        self.shape.y += dy

    def lanzar_lasers(self):
        laser = Laser(self.shape.centerx, self.shape.top)
        self.lasers.append(laser)

    def definir_dano(self):
        self.energia -= 10
        if self.energia <= 0:  # Cambiado para verificar si la energía es cero
            return True  # Significa que el personaje está muerto
        return False  # El personaje sigue vivo

    def dibujar(self, screen):
        screen.blit(self.image, self.shape.topleft)
        for laser in self.lasers:
            laser.dibujar(screen)
            laser.mover()

        # Dibujar la barra de energía
        pygame.draw.rect(screen, (255, 0, 0), (10, 10, 100, 10))
        pygame.draw.rect(screen, (0, 255, 0), (10, 10, self.energia, 10))

class Enemigo:
    def __init__(self, x, y):
        self.image = pygame.image.load(f'{ASSETS_PATH}/images/enemigo.png')
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect(topleft=(x, y))

    def mover(self):
        self.rect.y += 5  # velocidad del enemigo

    def dibujar(self, screen):
        screen.blit(self.image, self.rect.topleft)

class Laser:
    def __init__(self, x, y):
        self.image = pygame.image.load(f'{ASSETS_PATH}/images/laser1.png')
        self.rect = self.image.get_rect(center=(x, y))

    def mover(self):
        self.rect.y -= 10  # velocidad del laser

    def dibujar(self, screen):
        screen.blit(self.image, self.rect.topleft)
