from settings import *
import pygame


class Ennemy(pygame.sprite.Sprite):

    def __init__(self, pos, groups, player):
        super().__init__(groups)
        self.surface = pygame.display.get_surface()
        self.image = pygame.Surface((TILE_SIZE/2, TILE_SIZE))
        self.image.fill('yellow')
        self.rect = self.image.get_rect(topleft=pos)
        self.player = player
        self.max_life = 100
        self.life = 100
        self.attack_cooldown = 30
        self.damage = 20

    def update(self):
        self.attack_cooldown -= 1
        if self.life <= 0:
            self.kill()
            self.player.nb_kill += 1
            self.player.kill_reward()

    def attack(self):
        if self.attack_cooldown <= 0:
            self.player.pv -= self.damage
            self.attack_cooldown = 30
