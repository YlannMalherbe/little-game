import pygame
from game_data import *
from settings import *


class shop_title_nodes(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((200, 64))
        self.image.fill('grey')
        self.rect = self.image.get_rect(center=pos)


class shop_upgrade_nodes(pygame.sprite.Sprite):

    def __init__(self, pos, ratio):
        super().__init__()
        self.image = pygame.Surface((64, 64))
        self.image.fill('grey')
        self.pos_x = pos[0]
        self.pos_y = pos[1]
        self.rect = self.image.get_rect(center=(self.pos_x + 200 * ratio, self.pos_y))


class Overworld_Node(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((250, 64))
        self.image.fill('blue')
        self.rect = self.image.get_rect(center=pos)


class MarketPlace:

    def __init__(self, screen, stats, money, create_overworld, reload, current_level, max_level):
        self.display_surface = screen
        self.money = money
        self.stats = stats
        self.create_overworld = create_overworld
        self.reload = reload
        self.current_level = current_level
        self.max_level = max_level

        self.buying_cooldown = 20

        self.overworld_node = pygame.sprite.Group()

        self.screen_width = pygame.display.get_window_size()[0]
        self.screen_height = pygame.display.get_window_size()[1]

        self.screen_width_ratio = self.screen_width/DEFAULT_SCREEN_WIDTH
        self.screen_height_ratio = self.screen_height/DEFAULT_SCREEN_HEIGHT

        self.setup_shop()
        self.setup_button()
        self.setup_marketplace_node()

    def run(self):
        self.update_screen_size()
        self.shop_title_nodes.draw(self.display_surface)
        self.shop_upgrade_nodes.draw(self.display_surface)
        self.overworld_node.draw(self.display_surface)
        self.update_upgrade_level()
        self.update_tags()
        self.update_money()

        self.input()
        self.buying_cooldown -= 1

    def setup_marketplace_node(self):
        overworld_node = Overworld_Node((self.screen_width/2, self.screen_height-32))
        self.overworld_node.add(overworld_node)

    def setup_shop(self):
        self.shop_title_nodes = pygame.sprite.Group()
        for node_data in shop_info.values():
            pos_x = node_data["info"]['node_pos'][0]*self.screen_width_ratio
            pos_y = node_data["info"]['node_pos'][1]*self.screen_height_ratio
            node_sprite = shop_title_nodes((pos_x, pos_y))
            self.shop_title_nodes.add(node_sprite)

    def setup_button(self):
        self.shop_upgrade_nodes = pygame.sprite.Group()
        for node_data in shop_info.values():
            pos_x = node_data["info"]['node_pos'][0]*self.screen_width_ratio
            pos_y = node_data["info"]['node_pos'][1]*self.screen_height_ratio
            node_sprite = shop_upgrade_nodes((pos_x, pos_y), self.screen_width_ratio)
            self.shop_upgrade_nodes.add(node_sprite)

    def update_screen_size(self):
        old_screen_width = self.screen_width
        self.screen_width = pygame.display.get_window_size()[0]
        old_screen_height = self.screen_height
        self.screen_height = pygame.display.get_window_size()[1]

        self.screen_width_ratio = self.screen_width/DEFAULT_SCREEN_WIDTH
        self.screen_height_ratio = self.screen_height/DEFAULT_SCREEN_HEIGHT

        if old_screen_width != self.screen_width or old_screen_height != self.screen_height:
            self.reload(self.money)

    def update_tags(self):
        stats = ["speed", "attack_cooldown", "damage", "pv"]
        nb = 0
        for node_data in shop_info.values():
            upgrade = shop_info[str(nb)]["info"]["upgrade"]
            self.text_content = node_data['info']['Content']
            self.font = pygame.font.Font(None, 32)
            self.text_surface = self.font.render(self.text_content, True, BG_COLOR)
            pos_x = node_data["info"]['node_pos'][0] * self.screen_width_ratio
            pos_y = node_data["info"]['node_pos'][1] * self.screen_height_ratio
            self.text_rect = self.text_surface.get_rect(center=(pos_x, pos_y))

            self.display_surface.blit(self.text_surface, self.text_rect)
            self.text_content = "+"
            self.font = pygame.font.Font(None, 64)
            if self.money >= shop_info[str(nb)]["price"][self.stats[upgrade][1]] and self.stats[upgrade][1] < len(shop_info[str(nb)]["panel"])-1:
                self.text_surface = self.font.render(self.text_content, True, 'green')
            elif self.money >= shop_info[str(nb)]["price"][self.stats[upgrade][1]] and self.stats[upgrade][1] == len(shop_info[str(nb)]["panel"])-1:
                self.text_surface = self.font.render(self.text_content, True, BG_COLOR)
            else:
                self.text_surface = self.font.render(self.text_content, True, 'red')
            pos_x = node_data["info"]['node_pos'][0]
            pos_y = node_data["info"]['node_pos'][1]
            self.text_rect = self.text_surface.get_rect(center=((pos_x+200)*self.screen_width_ratio, (pos_y-4)*self.screen_height_ratio))
            self.display_surface.blit(self.text_surface, self.text_rect)

            self.text_content = f'{node_data["price"][self.stats[stats[nb]][1]]} gold'
            self.font = pygame.font.Font(None, 20)
            if self.money >= shop_info[str(nb)]["price"][self.stats[upgrade][1]] and self.stats[upgrade][1] < len(shop_info[str(nb)]["panel"])-1:
                self.text_surface = self.font.render(self.text_content, True, 'green')
            elif self.money >= shop_info[str(nb)]["price"][self.stats[upgrade][1]] and self.stats[upgrade][1] == len(shop_info[str(nb)]["panel"])-1:
                self.text_surface = self.font.render(self.text_content, True, BG_COLOR)
            else:
                self.text_surface = self.font.render(self.text_content, True, 'red')
            pos_x = node_data["info"]['node_pos'][0]
            pos_y = node_data["info"]['node_pos'][1]
            self.text_rect = self.text_surface.get_rect(center=((pos_x+200)*self.screen_width_ratio, (pos_y+16)*self.screen_height_ratio))
            self.display_surface.blit(self.text_surface, self.text_rect)
            nb += 1

        self.text_content = "Return"
        self.font = pygame.font.Font(None, 50)
        self.text_surface = self.font.render(self.text_content, True, 'White')
        self.text_rect = self.text_surface.get_rect(center=(self.screen_width/2, self.screen_height-32))
        self.display_surface.blit(self.text_surface, self.text_rect)

    def input(self):
        click_pos = pygame.mouse.get_pressed()[0]
        if click_pos:
            for sprite in self.overworld_node.sprites():
                if sprite.rect.collidepoint(pygame.mouse.get_pos()):
                    self.create_overworld(self.current_level, self.max_level, self.money, self.stats)
            nb = 0
            for sprite in self.shop_upgrade_nodes.sprites():
                if sprite.rect.collidepoint(pygame.mouse.get_pos()) and self.buying_cooldown <= 0:
                    upgrade = shop_info[str(nb)]["info"]["upgrade"]
                    if (self.stats[upgrade][1] + 1) < len(shop_info[str(nb)]["panel"]) and self.money >= shop_info[str(nb)]["price"][self.stats[upgrade][1]]:
                        self.money -= shop_info[str(nb)]["price"][self.stats[upgrade][1]]
                        self.stats[upgrade][1] += 1
                        self.stats[upgrade][0] = shop_info[str(nb)]["panel"][self.stats[upgrade][1]]

                    self.buying_cooldown = 20
                nb += 1

    def update_upgrade_level(self):
        total_lenght = 800
        space_between = 100
        stats = ["speed", "attack_cooldown", "damage", "pv"]
        stats_pos = 0
        for node_data in shop_info.values():
            nb_nodes = len(node_data["panel"])
            lenght = (total_lenght-space_between)/nb_nodes
            for nodes in range(nb_nodes):
                self.image = pygame.Surface((lenght, 64))
                if nodes <= self.stats[stats[stats_pos]][1]:
                    self.image.fill('green')
                else:
                    self.image.fill("grey")
                self.rect = self.image.get_rect(center=((total_lenght/nb_nodes*nodes + 500)*self.screen_width_ratio, (node_data['info']["node_pos"][1])*self.screen_height_ratio))
                self.display_surface.blit(self.image, self.rect)
            stats_pos += 1

    def update_money(self):
        self.text_content = f"{self.money} gold"
        self.text_surface = self.font.render(self.text_content, True, 'White')
        self.text_rect = self.text_surface.get_rect(topleft=(25, 600*self.screen_height_ratio))
        self.display_surface.blit(self.text_surface, self.text_rect)
