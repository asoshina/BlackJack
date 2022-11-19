import Player
from Deck import Deck
from Button import Button
from func_draw import *


class Game:
    max_pl_count = 5
    count = 0

    def __init__(self):
        self.players = []
        self.player = None
        self.player_pos = None
        self.dealer = Player.Dealer()
        self.all_players_count = 1
        self.deck = Deck()
        self.max_bet, self.min_bet = 20, 1
        # self.init = True

    def _launching(self):
        # Определяем количество ботов
        # while True:
        #     bots_count = is_int(f'\nHello! You should choose bots\' count for game(min = 0, max = {self.max_pl_count - 1}) ')
        #     if 0 <= bots_count <= self.max_pl_count - 1:
        #         break
        #     elif bots_count > 4:
        #         print(f'You enter number > {self.max_pl_count - 1}. Try again')
        #     else:
        #         print(f'You enter number < 0. Try again')
        bots_count = 4
        self.all_players_count = bots_count + 1
        # Создаем ботов

        for i in range(bots_count):
            b = Player.Bot(i)
            self.players.append(b)
            # print(b.name, ' is created')
            # print_text(str(b.name)+' is created', 20*i, 20*i)
            # i += 1
        self.player = Player.Player()
        self.player_pos = 2  # random.randint(0, self.all_players_count-1)
        # print('Your position is:', self.player_pos + 1)
        # print()
        self.players.insert(self.player_pos, self.player)
        # print(self.players)

    def ask_bet(self):
        for player in self.players:
            player.change_bet(self.max_bet, self.min_bet)
        # self.init = False

    def first_descr(self):
        for player in self.players:
            for _ in range(2):
                card = self.deck.get_card()
                player.take_card(card)

        card = self.deck.get_card()
        self.dealer.take_card(card)
        print_text('Dealer ', display_width//2-40, 20, font_size=15)
        self.dealer.print_cards()

    def check_stop(self, player):
        if player.full_points > 21:
            return True
        else:
            return False

    def fall_player(self, player):
        # player.print_cards()
        if isinstance(player, Player.Player):
            print('You are fall!')
        elif isinstance(player, Player.Bot):
            print(player.name, 'are fall!')
        # self.players.remove(player)
        print()

    def ask_cards(self, player):
        t = 0
        while True:
            if player.full_points > 21:
                self.fall_player(player)
                break
            elif player.full_points == 21:
                print('It\'s Black Jack')
                break
            else:
                if not player.ask_card():
                    if not isinstance(player, Player.Player):
                        print('Player doesn\'t want more cards')
                    break
                else:
                    t += 1
                    card = self.deck.get_card()
                    player.take_card(card)
                    draw_one_card(player, card, t)
                    draw_points(player)
                    print('Player takes card:', card)
                    print('Full points: ', player.full_points)

                    is_stop = self.check_stop(player)
                    if is_stop:
                        if player.full_points > 21 or isinstance(player, Player.Player):
                            self.fall_player(player)
                        break

                # if isinstance(player, Player.Player):
                #     player.print_cards()

    def check_winner(self):
        n = 0
        w = display_width // 2 - 70
        if self.dealer.full_points > 21:
            print_text('Dealer are fall!', w, display_height // 2 - 100)
            print_text('All players(full points <=21) in game are win!', w-115, display_height // 2 - 80)
            for winner in self.players:
                h = display_height // 2 - 60 + n * 20
                if winner.full_points <= 21:
                    winner.money += winner.bet * 2
                    if isinstance(winner, Player.Bot):
                        n += 1
                        print_text(winner.name + ' is win!', w, h)
                    elif isinstance(winner, Player.Player):
                        n += 1
                        print_text('You are win!', w, h)
                else:
                    if isinstance(winner, Player.Bot):
                        n += 1
                        print_text(winner.name + ' is lose!', w, h)
                    elif isinstance(winner, Player.Player):
                        n += 1
                        print_text('You are lose!', w, h)

        else:
            for player in self.players:
                h = display_height // 2 - 60 + n * 20
                if player.full_points <= 21:
                    # если количесто очков у игрока и дилера совпадают
                    if player.full_points == self.dealer.full_points:
                        player.money += player.bet
                        n += 1
                        print_text(f'{player.name} played in a draw!', w, h)
                    # если у игрока очков больше, чем у дилера
                    elif player.full_points > self.dealer.full_points:
                        player.money += player.bet * 2
                        if isinstance(player, Player.Bot):
                            n += 1
                            print_text(player.name + ' is win!', w, h)
                        elif isinstance(player, Player.Player):
                            n += 1
                            print_text('You are win!', w, h)

                    elif player.full_points < self.dealer.full_points:
                        if isinstance(player, Player.Bot):
                            n += 1
                            print_text(player.name + ' is lose!', w, h)
                        elif isinstance(player, Player.Player):
                            n += 1
                            print_text('You are lose!', w, h)
                else:
                    if isinstance(player, Player.Bot):
                        n += 1
                        print_text(player.name + ' is lose!', w, h)
                    elif isinstance(player, Player.Player):
                        n += 1
                        print_text('You are lose!', w, h)
        for player in self.players:
            draw_money(player)
        pygame.display.update()
        clock.tick(60)

    def play_with_dealer(self):
        t = 0
        while self.dealer.ask_card():
            card = self.deck.get_card()
            self.dealer.take_card(card)
            draw_dealer_cards(self.dealer, False, t)
            t += 1

    def enough_money(self):
        for player in self.players:
            if player.money <= 0:
                if isinstance(player, Player.Player):
                    clear(display_width // 2 - 185, display_height // 2 - 100, 410, 200)
                    print_text('You spent all your money. Game over', display_width // 2 - 115, display_height // 2 - 50)
                    wait()
                    self.clear_info()
                    self.show_menu()
                elif isinstance(player, Player.Bot):
                    clear(display_width // 2 - 185, display_height // 2 - 100, 410, 200)
                    print_text(str(player.name)+' spent all his money', display_width // 2 - 100, display_height // 2 - 50, font_size=14)
                    print_text('He\'s out of the game', display_width // 2 - 75, display_height // 2 - 30, font_size=14)
                    wait()
                    print(player.name, 'spent all his money. He\'s out of the game')
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
        self.player_pos = None
        self.dealer = Player.Dealer()
        self.all_players_count = 1
        self.deck = Deck()
        self.max_bet, self.min_bet = 20, 1
        # self.init = True

    def restart(self):
        clear(display_width // 2 - 185, display_height // 2 - 100, 410, 200)
        print_text('Wanna play again?', display_width // 2 - 55, display_height // 2 - 50)
        result = draw_yes_no()
        if result:
            self.one_more_play()
            return True
        else:
            self.clear_info()
            self.show_menu()
        pygame.display.update()
        clock.tick(60)

    def game_cycle(self):
        clear(0, 0, display_width, display_height)
        pygame.display.update()
        self._launching()

        while True:
            self.count = 1
            clear(0, 0, display_width, display_height)
            draw_first_screen(self)

            self.ask_bet()
            self.first_descr()

            for player in self.players:
                player.print_cards()
            for player in self.players:
                self.ask_cards(player)

            self.play_with_dealer()

            self.check_winner()

            wait()
            self.enough_money()
            # self.one_more_play()
            self.restart()
            # self.init = True
            # return game_over()

    def show_menu(self):

        # generating data for starting
        pygame.init()  # создаем окно

        menu_bckgr = pygame.image.load('Other/bcgr.jpeg')
        show = True
        start_btn = Button(220, 50)
        quit_btn = Button(100, 50)
        while show:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            display.blit(menu_bckgr, (0, 0))
            start_btn.draw(display_width // 2 - 75, display_height // 2 - 150, 'Start game', self.start_game, 40)
            quit_btn.draw(display_width // 2 - 25, display_height // 2 - 80, 'Quit', quit, 40)

            pygame.display.update()
            clock.tick(60)

    def start_game(self):
        while self.game_cycle():
            pass


# pygame.init()  # создаем окно
#
# need_input = False
# input_txt = '|'
# input_tick = 30
#
# show_menu()
# pygame.quit()
# quit()
