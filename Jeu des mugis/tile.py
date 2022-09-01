import pygame
from settings import *


class Tile(pygame.sprite.Sprite):

    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(TILE_COLOR)
        self.rect = self.image.get_rect(topleft=pos)


class DeathTile(Tile):

    def __init__(self, pos, groups):
        super().__init__(pos, groups)
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(DEATHTILE_COLOR)
        self.rect = self.image.get_rect(topleft=pos)


class VictoryTile(Tile):

    def __init__(self, pos, groups):
        super().__init__(pos, groups)
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(VICTORYTILE_COLOR)
        self.rect = self.image.get_rect(topleft=pos)


class CheckpointTile(Tile):

    def __init__(self, pos, groups, player):
        super().__init__(pos, groups)
        self.player = player
        self.player_spawn = self.player.spawn_point
        self.pos = pos
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(CHECKPOINTTILE_COLOR)
        self.rect = self.image.get_rect(topleft=self.pos)

    def update(self, player_spawn):
        if self.player_spawn != player_spawn:
            self.image.fill(TAKEN_CHECKPOINTTILE_COLOR)
