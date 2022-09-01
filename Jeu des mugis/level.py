import pygame.sprite
import pygame
import time
from random import randint
from settings import *
from tile import Tile, DeathTile, VictoryTile, CheckpointTile
from player import Player
from game_data import *
from ennemy import Ennemy

pygame.font.init()


class Level:

    def __init__(self, current_level, surface, create_overworld, money, stats):

        # level setup
        self.money = money
        self.display_surface = surface
        self.current_level = current_level
        self.level_data = levels[self.current_level]
        self.stats = stats

        self.screen_width = pygame.display.get_window_size()[0]
        self.screen_height = pygame.display.get_window_size()[1]
        # pre game setup
        self.text_content = self.level_data['level_content']
        self.font = pygame.font.Font(None, 50)
        self.text_surface = self.font.render(self.text_content, True, 'White')
        self.text_rect = self.text_surface.get_rect(center=(self.screen_width/2, self.screen_height/2))

        # sprite group setup
        self.visible_sprites = CameraGroup()
        self.active_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()
        self.death_sprites = pygame.sprite.Group()
        self.victory_sprites = pygame.sprite.Group()
        self.checkpoint_sprites = pygame.sprite.Group()

        self.mob_sprites = pygame.sprite.Group()

        # setup
        self.level_content = self.level_data['LEVEL_MAP']
        self.new_max_level = self.level_data['unlock']
        self.max_level = self.new_max_level - 1
        self.map_gravity = self.level_data['gravity']
        self.create_overworld = create_overworld

        self.pre_level()
        self.setup_level()

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            self.clear_screen()
            self.post_level(self.player.w_l, self.current_level)
            self.create_overworld(self.current_level, 0)

    def setup_level(self):
        for row_index, row in enumerate(self.level_content):
            for col_index, col in enumerate(row):
                x = col_index * TILE_SIZE
                y = row_index * TILE_SIZE
                if col == 'P':
                    self.player = Player((x, y), self.money, self.stats, self.map_gravity, [self.visible_sprites, self.active_sprites], self.collision_sprites, self.death_sprites, self.victory_sprites, self.checkpoint_sprites,self.mob_sprites)

        for row_index, row in enumerate(self.level_content):
            for col_index, col in enumerate(row):
                x = col_index * TILE_SIZE
                y = row_index * TILE_SIZE
                if col == 'X':
                    Tile((x, y), [self.visible_sprites, self.collision_sprites])
                if col == 'D':
                    DeathTile((x, y), [self.death_sprites, self.visible_sprites])
                if col == 'V':
                    VictoryTile((x, y), [self.victory_sprites, self.visible_sprites])
                if col == 'C':
                    CheckpointTile((x, y), [self.checkpoint_sprites, self.visible_sprites], self.player)
                if col == 'M':
                    Ennemy((x, y), [self.visible_sprites, self.active_sprites, self.mob_sprites], self.player)

    def attack(self):

        if self.player.cooldown == 0:
            self.player.image_attack = pygame.Surface((30, 60))
            self.player.image_attack.fill('red')

            direction = 0
            if self.player.facing_direction == "RIGHT":
                direction = 40
            elif self.player.facing_direction == "LEFT":
                direction = -40

            self.player.rect_attack = self.player.image_attack.get_rect(topleft=(self.player.rect.x + direction, self.player.rect.y))
            self.player.rect_attack.topleft -= self.visible_sprites.offset
            self.display_surface.blit(self.player.image_attack, self.player.rect_attack)

            self.player.cooldown = self.player.max_cooldown
            self.player.rect_attack.topleft += self.visible_sprites.offset
            self.player.attack_collide(self.player.rect_attack)

    def pre_level(self):
        self.display_surface.blit(self.text_surface, self.text_rect)
        pygame.display.update()
        time.sleep(1.5)

    def clear_screen(self):
        self.display_surface.fill(BG_COLOR)

    def post_level(self, w_l, current_level):
        pos = (self.screen_width / 2, self.screen_height / 2)
        if w_l == "win" and current_level < 4:
            self.choose_sentence(w_l)
            self.text_surface = self.font.render(self.sentence, True, 'White')
            self.text_rect = self.text_surface.get_rect(center=pos)
            self.display_surface.blit(self.text_surface, self.text_rect)
            pygame.display.update()
            time.sleep(1.5)
        if w_l == "win" and current_level == 4:
            self.choose_sentence("finish")
            line = 0
            for ligne in self.sentence.splitlines():
                self.text_rect = self.text_surface.get_rect(center=(self.screen_width / 2 - 70, self.screen_height / 2 + line*40))
                self.display_surface.blit(self.font.render(ligne, True, 'White'), self.text_rect)
                line += 1
            pygame.display.update()
            time.sleep(1.5)
        if w_l == "loose":
            self.choose_sentence(w_l)
            self.text_surface = self.font.render(self.sentence, True, 'White')
            self.text_rect = self.text_surface.get_rect(center=pos)
            self.display_surface.blit(self.text_surface, self.text_rect)
            pygame.display.update()
            time.sleep(1.5)
        if w_l == "dead":
            self.choose_sentence(w_l)
            self.text_surface = self.font.render(self.sentence, True, 'White')
            self.text_rect = self.text_surface.get_rect(center=pos)
            self.display_surface.blit(self.text_surface, self.text_rect)
            pygame.display.update()
            time.sleep(1.5)

    def choose_sentence(self, states):
        if states != "finish":
            nb = randint(0, len(end_level_sentence[states])-1)
            self.sentence = end_level_sentence[states][nb]
        if states == "finish":
            self.sentence = "GG you have finish our little game \n" \
                             "you can still redo the other level \n" \
                             "hope you had fun ;)"

    def update_screen_size(self):
        self.screen_width = pygame.display.get_window_size()[0]
        self.screen_height = pygame.display.get_window_size()[1]

        self.screen_width_ratio = self.screen_width/DEFAULT_SCREEN_WIDTH
        self.screen_height_ratio = self.screen_height/DEFAULT_SCREEN_HEIGHT

    def update_life(self):
        self.text_content = f"{self.player.life} life left"
        self.text_surface = self.font.render(self.text_content, True, 'White')
        self.text_rect = self.text_surface.get_rect(topleft=(20, 25))
        self.display_surface.blit(self.text_surface, self.text_rect)

    def update_pv(self):
        self.image = pygame.Surface((self.player.pv / self.player.max_pv * 300, 40))
        self.image.fill('red')
        self.rect = self.image.get_rect(topleft=(550*self.screen_width_ratio, 665*self.screen_height_ratio))
        self.display_surface.blit(self.image, self.rect)

        self.text_content = f"{self.player.pv} pv left"
        self.text_surface = self.font.render(self.text_content, True, 'White')
        self.text_rect = self.text_surface.get_rect(topleft=(555*self.screen_width_ratio, 670*self.screen_height_ratio))
        self.display_surface.blit(self.text_surface, self.text_rect)

    def update_kill(self):
        self.text_content = f"{self.player.nb_kill} kill"
        self.text_surface = self.font.render(self.text_content, True, 'White')
        self.text_rect = self.text_surface.get_rect(topleft=(20, 55))
        self.display_surface.blit(self.text_surface, self.text_rect)

    def update_money(self):
        self.text_content = f"{self.player.money} gold"
        self.text_surface = self.font.render(self.text_content, True, 'White')
        self.text_rect = self.text_surface.get_rect(topleft=(20, 85))
        self.display_surface.blit(self.text_surface, self.text_rect)

    def run(self):
        # run the entier game
        self.update_screen_size()
        self.active_sprites.update()
        self.checkpoint_sprites.update(self.player.spawn_point)
        self.visible_sprites.custom_draw(self.player)
        if self.player.attack:
            self.attack()
            self.player.attack = False
        self.input()
        self.update_life()
        self.update_pv()
        self.update_kill()
        self.update_money()
        if not self.player.level_states:
            old_money = self.money
            self.clear_screen()
            self.post_level(self.player.w_l, self.current_level)
            self.money = self.player.money
            if self.current_level != 4 and self.player.w_l != "dead":
                self.current_level += 1
            if self.player.w_l == "dead":
                self.new_max_level = self.current_level
                self.money = old_money
            self.create_overworld(self.current_level, self.new_max_level, self.money, self.stats)


class CameraGroup(pygame.sprite.Group):

    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2(100, 300)

        # Camera
        cam_left = CAMERA_BORDERS['left']
        cam_top = CAMERA_BORDERS['top']
        cam_width = self.display_surface.get_width() - (cam_left + CAMERA_BORDERS['right'])
        cam_height = self.display_surface.get_height() - (cam_top + CAMERA_BORDERS['bottom'])

        self.camera_rect = pygame.Rect(cam_left, cam_top, cam_width, cam_height)

    def custom_draw(self, player):

        # getting the camera pos
        if player.rect.left < self.camera_rect.left:
            self.camera_rect.left = player.rect.left
        if player.rect.right > self.camera_rect.right:
            self.camera_rect.right = player.rect.right

        if player.rect.bottom < self.camera_rect.bottom:
            self.camera_rect.bottom = player.rect.bottom
        if player.rect.top > self.camera_rect.top:
            self.camera_rect.top = player.rect.top

        # camera offset
        self.offset = pygame.math.Vector2(self.camera_rect.left - CAMERA_BORDERS['left'], self.camera_rect.top - CAMERA_BORDERS['top'])

        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)
