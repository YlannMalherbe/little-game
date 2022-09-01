import pygame
from game_data import levels
from settings import *


class Node(pygame.sprite.Sprite):
    def __init__(self, pos, status):
        super().__init__()
        self.image = pygame.Surface((100, 80))
        if status == 'done':
            self.image.fill('green')
        if status == 'available':
            self.image.fill('red')
        if status == 'locked':
            self.image.fill('grey')
        self.rect = self.image.get_rect(center=pos)


class MarketPlace_Node(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((250, 64))
        self.image.fill('blue')
        self.rect = self.image.get_rect(center=pos)


class Icon(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((32, 64))
        self.image.fill('#C4F7FF')
        self.rect = self.image.get_rect(center=pos)


class Overworld:

    def __init__(self, start_level, max_level, surface, create_level, create_marketplace, reload, money, stats):

        # setup
        self.reload = reload

        self.screen_width = pygame.display.get_window_size()[0]
        self.screen_height = pygame.display.get_window_size()[1]

        self.screen_width_ratio = self.screen_width/DEFAULT_SCREEN_WIDTH
        self.screen_height_ratio = self.screen_height/DEFAULT_SCREEN_HEIGHT

        self.display_surface = surface
        self.max_level = max_level
        self.current_level = start_level
        self.create_level = create_level
        self.create_marketplace = create_marketplace
        self.stats = stats

        self.marketplace_nodes = pygame.sprite.Group()

        self.money = money

        # movement logic
        self.speed = 8

        # sprites
        self.setup_nodes()
        self.setup_marketplace_node()
        self.setup_icon()

    def setup_nodes(self):
        self.nodes = pygame.sprite.Group()
        self.tag_data = []
        for index, node_data in enumerate(levels.values()):
            pos_x = node_data['node_pos'][0]*self.screen_width_ratio
            pos_y = node_data['node_pos'][1]*self.screen_height_ratio
            pos = [pos_x, pos_y]
            if index < self.max_level:
                nodes_sprite = Node(pos, 'done')
                self.tag_data.append([node_data['node_pos'], 'done'])
            elif index == self.max_level:
                nodes_sprite = Node(pos, 'available')
                self.tag_data.append([pos, 'available'])
            else:
                nodes_sprite = Node(pos, 'locked')
                self.tag_data.append([pos, 'locked'])
            self.nodes.add(nodes_sprite)

    def setup_marketplace_node(self):
        marketplace_node = MarketPlace_Node((self.screen_width/2, self.screen_height-32))
        self.marketplace_nodes.add(marketplace_node)

    def setup_icon(self):
        self.icon = pygame.sprite.GroupSingle()
        icon_sprite = Icon(self.nodes.sprites()[self.current_level].rect.center)
        self.icon.add(icon_sprite)

    def update_screen_size(self):
        old_screen_width = self.screen_width
        self.screen_width = pygame.display.get_window_size()[0]
        old_screen_height = self.screen_height
        self.screen_height = pygame.display.get_window_size()[1]

        self.screen_width_ratio = self.screen_width/DEFAULT_SCREEN_WIDTH
        self.screen_height_ratio = self.screen_height/DEFAULT_SCREEN_HEIGHT

        if old_screen_width != self.screen_width or old_screen_height != self.screen_height:
            self.reload(self.current_level, self.max_level, self.money, self.stats)

    def update_tag(self):
        level = 1
        for elt in self.tag_data:
            status = elt[1]
            pos_x = elt[0][0]
            pos_y = elt[0][1] + 70
            if status == 'done':
                self.text_content = f"Level - {level} - Done"
            if status == 'available':
                self.text_content = f"Level - {level} - available"
            if status == 'locked':
                self.text_content = f"Level - {level} - locked"
            self.font = pygame.font.Font(None, 50)
            self.text_surface = self.font.render(self.text_content, True, 'White')
            self.text_rect = self.text_surface.get_rect(center=(pos_x*self.screen_width_ratio, pos_y*self.screen_height_ratio))
            self.display_surface.blit(self.text_surface, self.text_rect)
            level += 1

        self.text_content = "MarketPlace"
        self.font = pygame.font.Font(None, 50)
        self.text_surface = self.font.render(self.text_content, True, 'White')
        self.text_rect = self.text_surface.get_rect(center=(self.screen_width/2, self.screen_height-32))
        self.display_surface.blit(self.text_surface, self.text_rect)

    def update_money(self):
        self.text_content = f"{self.money} gold"
        self.text_surface = self.font.render(self.text_content, True, 'White')
        self.text_rect = self.text_surface.get_rect(topleft=(25, 30))
        self.display_surface.blit(self.text_surface, self.text_rect)

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_z]:
            self.icon.sprite.rect.y -= self.speed
        if keys[pygame.K_q]:
            self.icon.sprite.rect.x -= self.speed
        if keys[pygame.K_s]:
            self.icon.sprite.rect.y += self.speed
        if keys[pygame.K_d]:
            self.icon.sprite.rect.x += self.speed

        for level in range(self.max_level+1):
            if level == 5:
                level = 4
            if keys[pygame.K_SPACE] and self.icon.sprite.rect.colliderect(self.nodes.sprites()[level]):
                self.create_level(level, self.money, self.stats)

        if keys[pygame.K_SPACE] and self.icon.sprite.rect.colliderect(self.marketplace_nodes.sprites()[0]):
            self.create_marketplace(self.money)

    def run(self):
        self.update_screen_size()
        self.input()
        self.marketplace_nodes.draw(self.display_surface)
        self.nodes.draw(self.display_surface)
        self.update_tag()
        self.update_money()
        self.icon.draw(self.display_surface)
