import Player
from const import *
from Func import print_text, get_input, clear, wait

pos = dict.fromkeys(pos_2.keys())
for x in pos:
    pos[x] = dict.fromkeys(pos_1.keys())
    for y in pos_1:
        pos[x][y] = (pos_2[x][0] + pos_1[y][0], pos_2[x][1] + pos_1[y][1])


def change_bet_draw():
    while True:
        print_text('Make your bet', (display_width // 2 - 50, display_height // 2 - 85))
        print_text('Min bet is $1  Max bet is $20', (display_width // 2 - 95, display_height // 2 - 60))
        result = get_input()
        clear(center, 410, 150)
        if result.isdigit():
            return int(result)
        else:
            print_text('Please, enter positive number', (display_width // 2 - 70, display_height // 2))


def draw_count_bot(n):
    while True:
        print_text(f'Please, enter number of bots (up to {n - 1})', (display_width // 2 - 110, display_height // 2 - 85))
        result = get_input()
        clear(center, 410, 150)
        if result.isdigit():
            return int(result)
        else:
            print_text('Please, enter a number', (display_width // 2 - 90, display_height // 2))


def draw_bot_bet(player):

    clear(pos[player.index]['bet'], 50, 20)
    print_text('Bet: $' + str(player.bet), pos[player.index]['bet'], font_size=15)

    pygame.display.update()
    clock.tick(60)


def draw_money(player):

    clear(pos[player.index]['money_value'], 50, 20)
    print_text('$' + str(player.money), pos[player.index]['money_value'], font_size=15)


def draw_dealer_cards(dealer, n=0):

    if n == -1:
        picture = cover
        sprite = pygame.image.load(picture)
        sprite = pygame.transform.rotozoom(sprite, 0, 0.3)
        display.blit(sprite, pos[dealer.index]['card'])
        dealer.full_points -= dealer.cards[0].points
        pygame.display.flip()
        pygame.time.delay(500)

        draw_card(dealer, 1)
        pygame.display.flip()
        pygame.time.delay(500)
    elif n == 0:
        draw_card(dealer, 0)
        draw_card(dealer, 1)
        pygame.display.flip()
        pygame.time.delay(500)
        dealer.full_points = sum([card.points for card in dealer.cards])
    else:
        draw_card(dealer, n+1)
        pygame.display.flip()
        pygame.time.delay(500)

    clear(pos[dealer.index]['points'], 100, 20)
    print_text('Points: '+str(dealer.full_points), pos[dealer.index]['points'], font_size=15)

    pygame.display.update()


def draw_points(player):

    clear(pos[player.index]['points'], 100, 20)
    print_text('Points: ' + str(player.full_points), pos[player.index]['points'], font_size=15)

    pygame.display.update()


def draw_card(player, n):

    picture = './Cards/' + player.cards[n].suit + '/' + player.cards[n].rank + '.png'
    sprite = pygame.image.load(picture)
    sprite = pygame.transform.rotozoom(sprite, 0, 0.3)

    display.blit(sprite, (pos[player.index]['card'][0]+n*30, pos[player.index]['card'][1]))

    pygame.display.update()
    clock.tick(60)


def draw_first_screen(game):

    for player in game.players:
        print_text(player.name, pos[player.index]['name'], font_size=20)
        print_text('Money ', pos[player.index]['money'], font_size=15)
        draw_money(player)
    print_text('Dealer ', pos[game.dealer.index]['name'], font_size=15)

    pygame.display.update()


def draw_yes_no():
    yes_btn = pygame.Rect(display_width // 2 - 45, display_height // 2, 50, 20)
    pygame.draw.rect(display, (255, 184, 0), yes_btn)
    print_text('Yes', (display_width // 2 - 35, display_height // 2), font_size=15)

    no_btn = pygame.Rect(display_width // 2 + 45, display_height // 2, 50, 20)
    pygame.draw.rect(display, (255, 184, 0), no_btn)
    print_text('No', (display_width // 2 + 65, display_height // 2), font_size=15)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse = pygame.mouse.get_pos()  # Location of the mouse-click
                if yes_btn.collidepoint(mouse):  # Was that click inside our rectangle
                    clear(center, 410, 150)
                    return True
                if no_btn.collidepoint(mouse):  # Was that click inside our rectangle
                    clear(center, 410, 150)
                    return False

        pygame.display.update()


def draw_decision(player):
    h = display_height // 2 - 50
    w = display_width // 2 - 80
    clear(center, 420, 150)
    if isinstance(player, Player.Bot):
        if player.full_points <= 21:
            print_text(player.name + ' doesn\'t want to take more cards!', (w, h), font_size=15)
        else:
            print_text(player.name + ' lost!', (w, h), font_size=15)
        wait()

