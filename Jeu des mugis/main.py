import sys
import json
import pygame
from settings import *
from level import Level
from overworld import Overworld
from marketplace import MarketPlace


def create_jsonfile(name_of_file, data_):
    with open(str(name_of_file)+'.txt', 'w') as data_name:
        json.dump(data_, data_name)


def open_file(name_of_file):
    with open(str(name_of_file)+'.txt') as data_stored:
        data_ = json.load(data_stored)
        return data_


data = {
    "max_level": 0,
    "current_level": 0,
    "money": 0,
    "stats": {
        "speed": [8, 1],
        "pv": [100, 1],
        "damage": [50, 3],
        "attack_cooldown": [20, 3]
    }
}

data = open_file('data')


class Game:

    def __init__(self):
        self.max_level = data["max_level"]
        self.current_level = data["current_level"]
        self.money = data["money"]
        self.stats = data["stats"]
        self.overworld = Overworld(self.current_level, self.max_level, screen, self.create_level, self.create_marketplace, self.create_overworld, self.money, self.stats)
        self.status = 'overworld'

    def create_level(self, current_level, money, stats):
        self.money = money
        self.current_level = current_level
        self.stats = stats
        self.level = Level(current_level, screen, self.create_overworld, self.money, self.stats)
        self.status = 'level'

    def create_marketplace(self, money):
        self.money = money
        self.marketplace = MarketPlace(screen, self.stats, self.money, self.create_overworld, self.create_marketplace, self.current_level, self.max_level)
        self.status = 'marketplace'

    def create_overworld(self, current_level, new_max_level, money, stats):
        self.money = money
        self.current_level = current_level
        self.stats = stats
        if new_max_level > self.max_level:
            self.max_level = new_max_level
        self.overworld = Overworld(current_level, self.max_level, screen, self.create_level, self.create_marketplace, self.create_overworld, self.money, self.stats)
        self.status = 'overworld'
            
    def run(self):
        if self.status == 'overworld':
            self.overworld.run()
        elif self.status == 'level':
            self.level.run()
        elif self.status == 'marketplace':
            self.marketplace.run()

    def save(self, data_):
        data_["current_level"] = self.current_level
        data_["max_level"] = self.max_level
        data_["money"] = self.money
        data_["stats"] = self.stats
        create_jsonfile("data", data_)


# Pygame setup
screen = pygame.display.set_mode((DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption('Jeu des mugis')
clock = pygame.time.Clock()

game = Game()

while True:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.save(data)
            pygame.quit()
            sys.exit()

    screen.fill(BG_COLOR)
    game.run()

    # Drawing logic
    pygame.display.update()
    clock.tick(60)
