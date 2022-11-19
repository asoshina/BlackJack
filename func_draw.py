import pygame
from const import clock, display_height, display_width, IMAGES, display
from Func import print_text


def change_bet_draw():
    while True:
        print_text('Make your bet', display_width // 2 - 50, display_height // 2 - 125)
        print_text('Min bet is 1  Max bet is 20', display_width // 2 - 95, display_height // 2 - 100)
        result = get_input()
        if result.isdigit():
            clear(display_width // 2 - 95, display_height // 2 - 125, 400, 200)
            return int(result)
        else:
            clear(display_width // 2 - 95, display_height // 2 - 125, 400, 200)
            print_text('Please, enter a number', display_width // 2 - 70, display_height // 2, font_color='red')


def draw_count_bot(n):
    while True:
        print_text('Choose bots\' count for game', display_width // 2 - 110, display_height // 2 - 125)
        print_text(f'min = 0, max = {n - 1}', display_width // 2 - 70, display_height // 2 - 100)
        result = get_input()
        if result.isdigit():
            clear(display_width // 2 - 115, display_height // 2 - 125, 400, 200)
            return int(result)
        else:
            clear(display_width // 2 - 115, display_height // 2 - 125, 400, 200)
            print_text('Please, enter a number', display_width // 2 - 90, display_height // 2, font_color='red')


def draw_bot_bet(player):
    if player.index == 0:
        clear_rect = pygame.Rect(display_width - 180, display_height // 2 + 55, 50, 20)
        pygame.draw.rect(display, 'white', clear_rect)
        print_text('Bet: ' + str(player.bet), display_width - 180, display_height // 2 + 55, font_size=15)
    elif player.index == 1:
        clear_rect = pygame.Rect(display_width-200, display_height-30, 50, 20)
        pygame.draw.rect(display, 'white', clear_rect)
        print_text('Bet: ' + str(player.bet),  display_width-200, display_height-30, font_size=15)
    elif player.index == 2:
        clear_rect = pygame.Rect(display_width//2-40, display_height-30, 50, 20)
        pygame.draw.rect(display, 'white', clear_rect)
        print_text('Bet: ' + str(player.bet), display_width//2-40, display_height-30, font_size=15)
    elif player.index == 3:
        clear_rect = pygame.Rect(100, display_height-30, 50, 20)
        pygame.draw.rect(display, 'white', clear_rect)
        print_text('Bet: ' + str(player.bet), 100, display_height-30, font_size=15)
    elif player.index == 4:
        clear_rect = pygame.Rect(20, display_height // 2 + 55, 50, 20)
        pygame.draw.rect(display, 'white', clear_rect)
        print_text('Bet: ' + str(player.bet), 20, display_height // 2 + 55, font_size=15)

    pygame.display.update()
    clock.tick(60)


def draw_money(player):
    if player.index == 0:
        clear_rect = pygame.Rect(display_width - 130, display_height // 2 - 120, 50, 20)
        pygame.draw.rect(display, 'white', clear_rect)
        print_text(str(player.money) + '$', display_width - 130, display_height // 2 - 120, font_size=15)
    elif player.index == 1:
        clear_rect = pygame.Rect(display_width - 145, display_height - 205, 50, 20)
        pygame.draw.rect(display, 'white', clear_rect)
        print_text(str(player.money) + '$', display_width - 145, display_height - 205, font_size=15)
    elif player.index == 2:
        clear_rect = pygame.Rect(display_width // 2 + 15, display_height - 205, 50, 20)
        pygame.draw.rect(display, 'white', clear_rect)
        print_text(str(player.money) + '$', display_width // 2 + 15, display_height - 205, font_size=15)
    elif player.index == 3:
        clear_rect = pygame.Rect(155, display_height - 205, 50, 20)
        pygame.draw.rect(display, 'white', clear_rect)
        print_text(str(player.money) + '$', 155, display_height - 205, font_size=15)
    elif player.index == 4:
        clear_rect = pygame.Rect(75, display_height // 2 - 120, 50, 20)
        pygame.draw.rect(display, 'white', clear_rect)
        print_text(str(player.money) + '$', 75, display_height // 2 - 120, font_size=15)


def draw_dealer_cards(dealer, flag, n=0):

    if flag:
        print_text('Points: ', display_width//2+15, 20, font_size=15)
        picture1 = './Cards/cover.png'
        sprite1 = pygame.image.load(picture1)
        sprite1 = pygame.transform.rotozoom(sprite1, 0, 0.3)
        display.blit(sprite1, (display_width//2-40, 40))

        picture2 = dealer.cards[0].picture
        sprite2 = pygame.image.load(picture2)
        sprite2 = pygame.transform.rotozoom(sprite2, 0, 0.3)
        display.blit(sprite2, (display_width//2-10, 40))
    elif n == 0:
        picture = dealer.cards[1].picture
        sprite = pygame.image.load(picture)
        sprite = pygame.transform.rotozoom(sprite, 0, 0.3)
        display.blit(sprite, (display_width//2-40, 40))

        picture = dealer.cards[0].picture
        sprite = pygame.image.load(picture)
        sprite = pygame.transform.rotozoom(sprite, 0, 0.3)
        display.blit(sprite, (display_width//2-10, 40))
    else:
        picture = dealer.cards[n+1].picture
        sprite = pygame.image.load(picture)
        sprite = pygame.transform.rotozoom(sprite, 0, 0.3)
        display.blit(sprite, (display_width // 2 - 10 + n*30, 40))

    clear_rect = pygame.Rect(display_width//2 + 70, 20, 100, 20)
    pygame.draw.rect(display, 'white', clear_rect)
    print_text(str(dealer.full_points), display_width//2 + 70, 20, font_size=15)

    pygame.display.update()
    clock.tick(60)


def draw_two_card(player):
    picture1 = IMAGES[player.cards[0].suit][player.cards[0].rank]
    sprite1 = pygame.image.load(picture1)
    sprite1 = pygame.transform.rotozoom(sprite1, 0, 0.3)

    picture2 = IMAGES[player.cards[1].suit][player.cards[1].rank]
    sprite2 = pygame.image.load(picture2)
    sprite2 = pygame.transform.rotozoom(sprite2, 0, 0.3)

    if player.index == 0:
        display.blit(sprite1, (display_width-200, display_height // 2 - 95))
        display.blit(sprite2, (display_width - 170, display_height // 2 - 95))
    elif player.index == 1:
        display.blit(sprite1, (display_width - 200, display_height - 180))
        display.blit(sprite2, (display_width-170, display_height-180))
    elif player.index == 2:
        display.blit(sprite1, (display_width // 2 - 40, display_height - 180))
        display.blit(sprite2, (display_width // 2 - 10, display_height - 180))
    elif player.index == 3:
        display.blit(sprite1, (100, display_height - 180))
        display.blit(sprite2, (130, display_height - 180))
    elif player.index == 4:
        display.blit(sprite1, (20, display_height // 2 - 95))
        display.blit(sprite2, (50, display_height // 2 - 95))

    pygame.display.update()
    clock.tick(60)


def draw_points(player):
    if player.index == 0:
        clear_rect = pygame.Rect(display_width - 125, display_height // 2 + 55, 100, 20)
        pygame.draw.rect(display, 'white', clear_rect)
        print_text('Points: ' + str(player.full_points), display_width - 125, display_height // 2 + 55, font_size=15)
    elif player.index == 1:
        clear_rect = pygame.Rect(display_width-145, display_height-30, 100, 20)
        pygame.draw.rect(display, 'white', clear_rect)
        print_text('Points: ' + str(player.full_points),  display_width-145, display_height-30, font_size=15)
    elif player.index == 2:
        clear_rect = pygame.Rect(display_width//2+10, display_height-30, 100, 20)
        pygame.draw.rect(display, 'white', clear_rect)
        print_text('Points: ' + str(player.full_points), display_width//2+15, display_height-30, font_size=15)
    elif player.index == 3:
        clear_rect = pygame.Rect(160, display_height-30, 100, 20)
        pygame.draw.rect(display, 'white', clear_rect)
        print_text('Points: ' + str(player.full_points), 160, display_height-30, font_size=15)
    elif player.index == 4:
        clear_rect = pygame.Rect(80, display_height // 2 + 55, 100, 20)
        pygame.draw.rect(display, 'white', clear_rect)
        print_text('Points: ' + str(player.full_points), 80, display_height // 2 + 55, font_size=15)

    pygame.display.update()
    clock.tick(60)


def draw_one_card(player, card, n):
    picture1 = card.picture
    sprite1 = pygame.image.load(picture1)
    sprite1 = pygame.transform.rotozoom(sprite1, 0, 0.3)

    if player.index == 0:
        display.blit(sprite1, (display_width-170+n*30, display_height // 2 - 95))
    elif player.index == 1:
        display.blit(sprite1, (display_width - 170 + n*30, display_height - 180))
    elif player.index == 2:
        display.blit(sprite1, (display_width // 2 - 10 + n*30, display_height - 180))
    elif player.index == 3:
        display.blit(sprite1, (130 + n*30, display_height - 180))
    elif player.index == 4:
        display.blit(sprite1, (50 + n*30, display_height // 2 - 95))

    pygame.display.update()
    clock.tick(60)


def draw_first_screen(game):
    for player in game.players:
        if player.index == 0:
            print_text(player.name, display_width - 190, display_height // 2 - 145, font_size=20)
            print_text('Money ', display_width - 190, display_height // 2 - 120, font_size=15)
        elif player.index == 1:
            print_text(player.name, display_width - 200, display_height - 230, font_size=20)
            print_text('Money ', display_width - 200, display_height - 205, font_size=15)
        elif player.index == 2:
            print_text(player.name, display_width // 2 - 40, display_height - 230, font_size=20)
            print_text('Money ', display_width // 2 - 40, display_height - 205, font_size=15)
        elif player.index == 3:
            print_text(player.name, 100, display_height - 230, font_size=20)
            print_text('Money ', 100, display_height - 205, font_size=15)
        elif player.index == 4:
            print_text(player.name, 20, display_height // 2 - 145, font_size=20)
            print_text('Money ', 20, display_height // 2 - 120, font_size=15)
        draw_money(player)
    print_text('Dealer ', display_width // 2 - 40, 20, font_size=15)


    pygame.display.update()
    clock.tick(60)


def draw_yes_no():
    yes_btn = pygame.Rect(display_width // 2 - 45, display_height // 2, 50, 20)
    pygame.draw.rect(display, (255, 184, 0), yes_btn)
    print_text('Yes', display_width // 2 - 35, display_height // 2, font_size=15)

    no_btn = pygame.Rect(display_width // 2 + 45, display_height // 2, 50, 20)
    pygame.draw.rect(display, (255, 184, 0), no_btn)
    print_text('No', display_width // 2 + 65, display_height // 2, font_size=15)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse = pygame.mouse.get_pos()  # Location of the mouse-click
                if yes_btn.collidepoint(mouse):  # Was that click inside our rectangle
                    clear_rect = pygame.Rect(display_width // 2 - 100, display_height // 2 - 100, 400, 200)
                    pygame.draw.rect(display, 'white', clear_rect)
                    return True
                if no_btn.collidepoint(mouse):  # Was that click inside our rectangle
                    clear_rect = pygame.Rect(display_width // 2 - 100, display_height // 2 - 100, 400, 200)
                    pygame.draw.rect(display, 'white', clear_rect)
                    return False

        pygame.display.update()
        clock.tick(60)


def get_input():
    need_input = True
    input_txt = ''
    input_tick = 30
    input_rect = pygame.Rect(display_width // 2 - 30, display_height // 2 - 50, 70, 30)
    pygame.draw.rect(display, (255, 184, 0), input_rect)
    while True:
        for event in pygame.event.get():
            # mouse = pygame.mouse.get_pos()
            # click = pygame.mouse.get_pressed()
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                # input_txt = input_txt.replace('|', '')
                # input_tick = 30
                if event.key == pygame.K_RETURN:
                    return input_txt.strip()
                    # need_input = False
                    # input_txt = ''
                elif event.key == pygame.K_BACKSPACE:
                    print(input_txt)
                    input_txt = input_txt[:-1:]
                    print(input_txt)
                else:
                    if len(input_txt) < 10:
                        input_txt += event.unicode
                # input_txt += '|'
        pygame.draw.rect(display, (255, 184, 0), input_rect)
        print_text(message=input_txt, x=input_rect.x+10, y=input_rect.y+5)
        # input_tick -= 1
        # if input_tick == 0:
        #     input_txt = input_txt[:-1:]
        # if input_tick == -30:
        #     input_txt += '|'
        #     input_tick = 30
        pygame.display.update()
        clock.tick(60)


def clear(point_x, point_y, width, height):
    clear_rect = pygame.Rect(point_x, point_y, width, height)
    pygame.draw.rect(display, 'white', clear_rect)
    pygame.display.update()


def wait():
    flag = True
    while True and flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    flag = False
                    break
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
        pygame.display.update()
        clock.tick(60)
