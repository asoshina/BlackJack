# import pygame
from const import *


def is_int(x):
    while True:
        s = input(f'{x}')
        try:
            s = int(s)
        except ValueError:
            print("Some value was incorrect! Enter number")
        else:
            return s


def print_text(message, x, y, font_color='Black', font_type='./Other/OpenSans-Regular.ttf', font_size=20):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_size)
    display.blit(text, (x, y))


def get_input():
    input_rect = pygame.Rect(20, 400, 250, 70)
    pygame.draw.rect(display, 'red', input_rect)

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if input_rect.collidepoint(mouse[0], mouse[1]) and click[0]:
        need_input = True

    if need_input:
        for event in pygame.event.get():
            if need_input and event.type == pygame.KEYDOWN:
                input_txt = input_txt.replace('|', '')
                input_tick = 30
                if event.key == pygame.K_RETURN:
                    need_input = False
                    input_txt = ''
                elif event.key == pygame.K_BACKSPACE:
                    input_txt = input_txt[:-1:]
                else:
                    if len(input_txt) < 10:
                        input_txt += event.unicode
                input_txt += '|'
        print_text(message=input_txt, x=input_rect.x + 10, y=input_rect.y + 10)
        input_tick -= 1
        if input_tick == 0:
            input_txt = input_txt[:-1:]
        if input_tick == -30:
            input_txt += '|'
            input_tick = 30
        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_TAB]:
        #     need_input = True