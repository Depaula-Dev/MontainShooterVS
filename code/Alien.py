import pygame
from code.Entity import Entity
from code.AlienShot import AlienShot
from code.Const import (
    ENTITY_SHOT_DELAY, ENTITY_SPEED, PLAYER_KEY_DOWN, PLAYER_KEY_LEFT,
    PLAYER_KEY_RIGHT, PLAYER_KEY_SHOT, PLAYER_KEY_UP, WIN_HEIGHT, WIN_WIDTH
)


class Alien(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

    def move(self):
        keys = pygame.key.get_pressed()
        
        if keys[PLAYER_KEY_UP[self.name]] and self.rect.top > 0:
            self.rect.centery -= ENTITY_SPEED[self.name]
        if keys[PLAYER_KEY_DOWN[self.name]] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += ENTITY_SPEED[self.name]
        if keys[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
        if keys[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]

    def shot(self):
        keys = pygame.key.get_pressed()

        if keys[PLAYER_KEY_SHOT[self.name]] and self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return AlienShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.top - 10))

        if self.shot_delay > 0:
            self.shot_delay -= 1
        
        return None
