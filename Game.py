import Player
from Deck import Deck
from Button import Button
from func_draw import *
from Func import *
import pygame

class Game:
    max_pl_count = 5
    count = 0

    def __init__(self):
        self.players = []
        self.player = None
        self.dealer = Player.Dealer()
        self.all_players_count = 1
        self.deck = Deck()
        self.max_bet, self.min_bet = 20, 1

    def _launching(self):

        # choose count of bots
        while True:
            bots_count = draw_count_bot(self.max_pl_count)
            if bots_count < self.max_pl_count:
                break

            x = display_width // 2 - 115
            y = display_height // 2
            print_text(f'You enter number >= {self.max_pl_count}. Try again', (x, y))

        self.all_players_count = bots_count + 1

        # Create bots and choose their place
        for i in range(bots_count):
            b = Player.Bot()
            if i == 1:
                b.index = 4
            if i == 2:
                b.index = 1
            if i == 3:
                b.index = 3
            self.players.append(b)

        self.player = Player.Player()
        self.player.index = 2  # bottom position
        self.players.append(self.player)
        self.players.sort(key=lambda x: x.index)

    def ask_bet(self):
        for player in self.players:
            player.change_bet(self.max_bet, self.min_bet)
            pygame.display.flip()
            pygame.time.delay(500)

    def set_cards(self):
        for player in self.players:
            for _ in range(2):
                card = self.deck.get_card()
                player.take_card(card)

        for _ in range(2):
            card = self.deck.get_card()
            self.dealer.take_card(card)

        self.dealer.print_cards()

    def ask_cards(self, player):
        t = 2
        while True:
            if player.full_points > 21:
                # self.fall_player(player)
                break
            elif player.full_points == 21:
                break
            else:
                if not player.ask_card():
                    break
                else:
                    card = self.deck.get_card()
                    player.take_card(card)
                    draw_card(player, t)
                    draw_points(player)
                    t += 1
                    pygame.display.flip()
                    pygame.time.delay(500)

    def check_winner(self):
        clear(center, 410, 150)
        w = display_width // 2 - 70
        if self.dealer.full_points > 21:
            print_text('Dealer lost!', (w, display_height // 2 - 85))
            for n, player in enumerate(self.players):
                h = display_height // 2 - 50 + n * 20
                if player.full_points <= 21:
                    player.money += player.bet * 2
                    print_text(player.name + ' won!', (w, h), font_size=15)
                else:
                    print_text(player.name + ' lost!', (w, h), font_size=15)

        else:
            for n, player in enumerate(self.players):
                h = display_height // 2 - 50 + n * 20
                if player.full_points <= 21:
                    # если количесто очков у игрока и дилера совпадают
                    if player.full_points == self.dealer.full_points:
                        player.money += player.bet
                        print_text(f'{player.name} played in a draw!', (w, h), font_size=15)
                    # если у игрока очков больше, чем у дилера
                    elif player.full_points > self.dealer.full_points:
                        player.money += player.bet * 2
                        print_text(player.name + ' won!', (w, h), font_size=15)

                    elif player.full_points < self.dealer.full_points:
                        print_text(player.name + ' lost!', (w, h), font_size=15)
                else:
                    print_text(player.name + ' lost!', (w, h), font_size=15)
        for player in self.players:
            draw_money(player)
        pygame.display.update()
        clock.tick(60)

    def play_with_dealer(self):
        draw_dealer_cards(self.dealer, 0)
        t = 1
        while self.dealer.ask_card():
            card = self.deck.get_card()
            self.dealer.take_card(card)
            draw_dealer_cards(self.dealer, t)
            t += 1


    def enough_money(self):
        for player in self.players:
            if player.money <= 0:
                if isinstance(player, Player.Player):
                    clear(center, 410, 200)
                    print_text('You spent all your money. Game over', (display_width // 2 - 115, display_height // 2 - 50))
                    wait()
                    self.clear_info()
                    self.show_menu()
                elif isinstance(player, Player.Bot):
                    clear(center, 410, 200)
                    print_text(str(player.name)+' spent all his money', (display_width // 2 - 100, display_height // 2 - 50), font_size=14)
                    print_text('He\'s out of the game', (display_width // 2 - 75, display_height // 2 - 30), font_size=14)
                    wait()
                    self.players.remove(player)

    def one_more_play(self):
        if self.count > 0:
            for player in self.players:
                player.full_points = 0
                player.cards = []
            self.dealer.full_points = 0
            self.dealer.cards = []
            self.deck = Deck()

    def clear_info(self):
        self.players = []
        self.player = None
        self.dealer = Player.Dealer()
        self.all_players_count = 1
        self.deck = Deck()
        self.max_bet, self.min_bet = 20, 1

    def restart(self):
        clear(center, 410, 150)
        print_text('Wanna play again?', (display_width // 2 - 55, display_height // 2 - 50))
        result = draw_yes_no()
        if result:
            self.one_more_play()
            return True
        else:
            self.clear_info()
            self.show_menu()
        pygame.display.update()

    def start_game(self):
        clear((0, 0), display_width, display_height)
        pygame.display.update()
        self._launching()

        while True:
            self.count = 1
            clear((0, 0), display_width, display_height)
            draw_first_screen(self)

            self.ask_bet()
            self.set_cards()

            for player in self.players:
                player.print_cards()
            for player in self.players:
                self.ask_cards(player)
                draw_decision(player)

            self.play_with_dealer()

            self.check_winner()

            wait()
            self.enough_money()
            self.restart()

    def show_menu(self):

        # generating data for starting
        pygame.init()  # создаем окно

        menu_background = pygame.image.load(background_menu)
        show = True
        start_btn = Button(220, 50)
        quit_btn = Button(100, 50)
        while show:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            display.blit(menu_background, (0, 0))
            start_btn.draw(display_width // 2 - 75, display_height // 2 - 150, 'Start game', self.start_game, 40)
            quit_btn.draw(display_width // 2 - 25, display_height // 2 - 80, 'Quit', quit, 40)

            pygame.display.update()
            clock.tick(15)
