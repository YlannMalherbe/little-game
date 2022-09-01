import random

import pygame
from settings import *


class Player(pygame.sprite.Sprite):

    def __init__(self, pos, money, stats, gravity, groups, collision_sprites, death_sprites, victory_sprites, checkpoint_sprites, ennemies_sprites):
        super().__init__(groups)

        self.display_surface = pygame.display.get_surface()
        self.spawn_point = pos
        self.image = pygame.Surface((TILE_SIZE//2, TILE_SIZE))
        self.image.fill(PLAYER_COLOR)
        self.rect = self.image.get_rect(topleft=pos)
        self.level_states = True
        self.w_l = "loose"

        # player attack
        self.attack = False
        self.facing_direction = 'RIGHT'

        # player stats
        self.nb_kill = 0
        self.money = money

        # player stats
        self.stats = stats
        self.cooldown = self.stats["attack_cooldown"][0]
        self.max_cooldown = self.stats["attack_cooldown"][0]
        self.damage = self.stats["damage"][0]
        self.life = 5
        self.pv = self.stats["pv"][0]
        self.max_pv = self.stats["pv"][0]
        self.speed = self.stats["speed"][0]

        # Player movement
        self.direction = pygame.math.Vector2()
        self.gravity = gravity
        self.jump_speed = 16
        self.collision_sprites = collision_sprites
        self.death_sprites = death_sprites
        self.victory_sprites = victory_sprites
        self.checkpoint_sprites = checkpoint_sprites
        self.ennemies_sprites = ennemies_sprites
        self.on_floor = False

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.direction.x = 1
            self.facing_direction = "RIGHT"
        elif keys[pygame.K_q]:
            self.direction.x = -1
            self.facing_direction = "LEFT"
        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE] and self.on_floor:
            self.direction.y = -self.jump_speed

        if keys[pygame.K_e]:
            self.attack = True

    def respawn(self):
        self.rect = self.image.get_rect(topleft=self.spawn_point)

    def horizontal_collisions(self):
        for sprite in self.collision_sprites.sprites():
            if sprite.rect.colliderect(self.rect):
                if self.direction.x < 0:
                    self.rect.left = sprite.rect.right
                if self.direction.x > 0:
                    self.rect.right = sprite.rect.left
        for sprite in self.death_sprites.sprites():
            if sprite.rect.colliderect(self.rect):
                self.life -= 1
                self.respawn()
                self.pv = self.stats["pv"][0]
        for sprite in self.victory_sprites.sprites():
            if sprite.rect.colliderect(self.rect):
                self.level_states = False
                self.w_l = "win"
        for sprite in self.checkpoint_sprites.sprites():
            if sprite.rect.colliderect(self.rect):
                self.spawn_point = self.rect.topleft
        for sprite in self.ennemies_sprites.sprites():
            if sprite.rect.colliderect(self.rect):
                sprite.attack()

    def vertical_collisions(self):
        for sprite in self.collision_sprites.sprites():
            if sprite.rect.colliderect(self.rect):
                if self.direction.y > 0:
                    self.rect.bottom = sprite.rect.top
                    self.direction.y = 0
                    self.on_floor = True
                if self.direction.y < 0:
                    self.rect.top = sprite.rect.bottom
                    self.direction.y = 0
        for sprite in self.death_sprites.sprites():
            if sprite.rect.colliderect(self.rect):
                self.life -= 1
                self.respawn()
                self.pv = self.stats["pv"][0]
        for sprite in self.victory_sprites.sprites():
            if sprite.rect.colliderect(self.rect):
                self.level_states = False
                self.w_l = "win"
        for sprite in self.checkpoint_sprites.sprites():
            if sprite.rect.colliderect(self.rect):
                self.spawn_point = self.rect.topleft

        if self.on_floor and self.direction.y != 0:
            self.on_floor = False

    def attack_collide(self, attack_rect):
        for sprite in self.ennemies_sprites.sprites():
            if sprite.rect.colliderect(attack_rect):
                sprite.life -= self.damage

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def check_life(self):
        if self.pv == 0:
            self.life -= 1
            self.respawn()
            self.pv = self.stats["pv"][0]
        if self.life == 0:
            self.level_states = False
            self.w_l = 'dead'

    def kill_reward(self):
        money_gain = random.randint(3, 20)
        self.money += money_gain

    def update(self):
        self.input()
        self.rect.x += self.direction.x * self.speed
        self.horizontal_collisions()
        self.apply_gravity()
        self.vertical_collisions()
        self.check_life()
        if self.cooldown >= 1:
            self.cooldown -= 1
