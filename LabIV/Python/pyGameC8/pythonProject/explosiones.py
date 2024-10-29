import pygame
import os
from constantes import ASSETS_PATH

class Explosion:
    def __init__(self, x, y):
        self.images = [pygame.image.load(f'{ASSETS_PATH}/images/regularExplosion000.png') for i in range(9)]
        self.index = 0
        self.rect = self.images[self.index].get_rect(center=(x, y))
        self.frame_rate = 0
        self.max_frame = 5  # Añadido para controlar la velocidad de la animación

    # Actualizar la pantalla
    def actualizar(self):
        self.frame_rate += 1
        if self.frame_rate >= self.max_frame:
            self.frame_rate = 0
            self.index += 1
            if self.index >= len(self.images):
                return False
        return True

    def dibujar(self, screen):
        screen.blit(self.images[self.index], self.rect.topleft)  # Cambiado a images y rect
