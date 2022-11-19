import abc
import random
from const import MESSAGES, NAMES
from Func import print_text
from Func import is_int
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
            draw_dealer_cards(self, True)
        elif isinstance(self, Player):
            draw_two_card(self)
            draw_points(self)
        elif isinstance(self, Bot):
            draw_two_card(self)
            draw_points(self)


class Player(AbstractPlayer):
    def __init__(self):
        super().__init__()
        self.name = 'You'
        self.index = 2

    def change_bet(self, max_bet, min_bet):
        while True:
            value = change_bet_draw()
            if value > self.money:
                print_text('Your haven\'t enough money', display_width // 2 - 70, display_height // 2)
            elif max_bet >= value >= min_bet and value <= self.money:
                self.bet = value
                self.money -= self.bet
                break
            else:
                print_text('Your bet is too big or too small', display_width // 2 - 70, display_height // 2)

        draw_bot_bet(self)
        draw_money(self)

    def ask_card(self):
        while True:
            print_text('One more card?', display_width // 2 - 50, display_height // 2 - 50)
            result = draw_yes_no()
            if result:
                return True
            elif not result:
                return False


class Bot(AbstractPlayer):

    def __init__(self, index):
        super().__init__()
        self.max_points = random.randint(17, 20)
        self.name = 'Bot ' + random.choice(NAMES)
        if index < 2:
            self.index = index
        else:
            self.index = index + 1

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

    def change_bet(self, max_bet, min_bet):
        """
        NOTE: This type is Dealer so it has no bets
        """""
        raise Exception('This type is dealer so it has no bets')

    def ask_card(self):
        if self.full_points < self.max_points:
            return True
        else:
            return False
