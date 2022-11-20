import pygame
import os

dirname = os.path.dirname(os.path.abspath(__file__))
display_width = 1000
display_height = 650

display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("BlackJack")

icon = pygame.image.load(dirname+'/Other/icon.jpeg')
pygame.display.set_icon(icon)

clock = pygame.time.Clock()
pos_2 = {0: (display_width - 190, display_height // 2 - 150),
         1: (display_width - 200, display_height - 230),
         2: (display_width // 2 - 40,display_height - 230),
         3: (100, display_height - 230),
         4: (20, display_height // 2 - 150),
         6: (display_width // 2 - 40, 10)
         }

pos_1 = {
        'name': (0, 0),
        'money': (-10, 30),
        'money_value': (40, 30),
        'points': (0, 210),
        'bet': (90, 30),
        'card': (-10,  55)
    }

center = (display_width // 2 - 185, display_height // 2 - 85)

SUITS = ['heart', 'diamond', 'club', 'spade']
RANKS = {'2': 2,
         '3': 3,
         '4': 4,
         '5': 5,
         '6': 6,
         '7': 7,
         '8': 8,
         '9': 9,
         '10': 10,
         'jack': 10,
         'queen': 10,
         'king': 10,
         'ace': 11
         }

cover = './Cards/cover.png'
background_menu = 'Other/bcgr.jpeg'

NAMES = ['John', 'Jack', 'Mary', 'Peter', 'Jane', 'Clark', 'Teddy', 'Joseph', 'Anna', 'Bobby', 'Denny', 'Frank',
         'Harry', 'Ivan', 'Kan', 'Molly', 'Ned', 'Olaf', 'Randy', 'Tom', 'Oliver', 'Jacob', 'Charley',
         'Thomas', 'George', 'Oscar', 'Jason', 'Noah', 'Liam', 'William', 'Mason', 'James', 'Benjamin',
         'Michael', 'Emma', 'Sophia', 'Charlotte', 'Harper', 'Emily']
