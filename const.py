import pygame
display_width = 1000  # ширина игрового окна
display_height = 650  # высота игрового окна

display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("BlackJack")  # заголовок окна

icon = pygame.image.load('Cards/J4.png')  # иконка окна
pygame.display.set_icon(icon)

clock = pygame.time.Clock()  # с какой частатой будет обнавляться экран


SUITS = ['heart', 'diamond', 'club', 'spade']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
IMAGES = {'spade':
              {'ace': './Cards/A_Spades.png',
               'king': './Cards/K_Spades.png',
               'queen': './Cards/Q_Spades.png',
               'jack': './Cards/J_Spades.png',
               '10': './Cards/10_Spades.png',
               '9': './Cards/9_Spades.png',
               '8': './Cards/8_Spades.png',
               '7': './Cards/7_Spades.png',
               '6': './Cards/6_Spades.png',
               '5': './Cards/5_Spades.png',
               '4': './Cards/4_Spades.png',
               '3': './Cards/3_Spades.png',
               '2': './Cards/2_Spades.png'},
          'heart':
              {'ace': './Cards/A_Spades.png',
               'king': './Cards/K_Spades.png',
               'queen': './Cards/Q_Spades.png',
               'jack': './Cards/J_Spades.png',
               '10': './Cards/10_Spades.png',
               '9': './Cards/9_Spades.png',
               '8': './Cards/8_Spades.png',
               '7': './Cards/7_Spades.png',
               '6': './Cards/6_Spades.png',
               '5': './Cards/5_Spades.png',
               '4': './Cards/4_Spades.png',
               '3': './Cards/3_Spades.png',
               '2': './Cards/2_Spades.png'},
          'diamond':
              {'ace': './Cards/A_Spades.png',
               'king': './Cards/K_Spades.png',
               'queen': './Cards/Q_Spades.png',
               'jack': './Cards/J_Spades.png',
               '10': './Cards/10_Spades.png',
               '9': './Cards/9_Spades.png',
               '8': './Cards/8_Spades.png',
               '7': './Cards/7_Spades.png',
               '6': './Cards/6_Spades.png',
               '5': './Cards/5_Spades.png',
               '4': './Cards/4_Spades.png',
               '3': './Cards/3_Spades.png',
               '2': './Cards/2_Spades.png'},
          'club':
              {'ace': './Cards/A_Spades.png',
               'king': './Cards/K_Spades.png',
               'queen': './Cards/Q_Spades.png',
               'jack': './Cards/J_Spades.png',
               '10': './Cards/10_Spades.png',
               '9': './Cards/9_Spades.png',
               '8': './Cards/8_Spades.png',
               '7': './Cards/7_Spades.png',
               '6': './Cards/6_Spades.png',
               '5': './Cards/5_Spades.png',
               '4': './Cards/4_Spades.png',
               '3': './Cards/3_Spades.png',
               '2': './Cards/2_Spades.png'}
          }

MESSAGES = {
    'ask_start': 'Do you want to play Black Jack?(y/n) ',
    'ask_card': 'Want new card?(y/n) ',
    'eq': '{player} has {points} points so it equals with dealer points\n{player} bid will be back.',
    'win': '{} player are win.',
    'lose': '{} player are lose.',
    'rerun': 'Wanna play again?(y/n) '
}

NAMES = ['John', 'Jack', 'Mary', 'Peter', 'Jane', 'Clark', 'Teddy', 'Joseph', 'Anna', 'Bobby', 'Denny', 'Frank',
         'Harry', 'Ivan', 'Kan', 'Molly', 'Ned', 'Olaf', 'Randy', 'Tom', 'Oliver', 'Jacob', 'Charley',
         'Thomas', 'George', 'Oscar', 'Jason', 'Noah', 'Liam', 'William', 'Mason', 'James', 'Benjamin',
         'Michael', 'Emma', 'Sophia', 'Charlotte', 'Harper', 'Emily']
