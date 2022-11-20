import abc
import random
from func_draw import *


class AbstractPlayer(abc.ABC):

    def __init__(self):
        self.cards = []
        self.bet = 0
        self.full_points = 0
        self.money = 100
        self.name = None
        self.index = 0
        self.bool = True

    def change_points(self):
        self.full_points = sum([card.points for card in self.cards])
        if self.full_points > 21:
            for card in self.cards:
                if card.rank == 'ace':
                    self.full_points -= 10

    def take_card(self, card):
        self.cards.append(card)
        self.change_points()

    @abc.abstractmethod
    def change_bet(self,  max_bet, min_bet):
        pass

    @abc.abstractmethod
    def ask_card(self):
        pass

    def print_cards(self):
        if isinstance(self, Dealer):
            draw_dealer_cards(self, -1)
        else:
            draw_card(self, 0)
            pygame.display.flip()
            pygame.time.delay(500)
            draw_card(self, 1)
            draw_points(self)
            pygame.display.flip()
            pygame.time.delay(500)



class Player(AbstractPlayer):
    def __init__(self):
        super().__init__()
        self.name = 'You'
        self.index = 2

    def change_bet(self, max_bet, min_bet):
        while True:
            value = change_bet_draw()
            if value > self.money:
                print_text('Your haven\'t enough money', (display_width // 2 - 70, display_height // 2))
            elif max_bet >= value >= min_bet and value <= self.money:
                self.bet = value
                self.money -= self.bet
                break
            else:
                print_text('Your bet is too big or too small', (display_width // 2 - 70, display_height // 2))

        draw_bot_bet(self)
        draw_money(self)

    def ask_card(self):
        while True:
            clear(center, 410, 150)
            print_text('One more card?', (display_width // 2 - 50, display_height // 2 - 50))
            result = draw_yes_no()
            if result:
                return True
            elif not result:
                return False


class Bot(AbstractPlayer):

    def __init__(self):
        super().__init__()
        self.max_points = random.randint(17, 20)
        self.name = 'Bot ' + random.choice(NAMES)
        self.index = 0

    def change_bet(self, max_bet, min_bet):
        if 0 < self.money < max_bet:
            self.bet = random.randint(min_bet, self.money)
        else:
            self.bet = random.randint(min_bet, max_bet)
        self.money -= self.bet
        draw_bot_bet(self)
        draw_money(self)

    def ask_card(self):
        if self.full_points < self.max_points:
            return True
        else:
            return False


class Dealer(AbstractPlayer):

    max_points = 17

    def __init__(self):
        super().__init__()
        self.name = 'Dealer'
        self.index = 6

    def change_bet(self, max_bet, min_bet):
        # """
        # NOTE: This type is Dealer so it has no bets
        # """""
        # raise Exception('This type is dealer so it has no bets')
        pass

    def ask_card(self):
        if self.full_points < self.max_points:
            return True
        else:
            return False
