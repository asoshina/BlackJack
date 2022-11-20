from itertools import product
from random import shuffle
from const import SUITS, RANKS


class Card:

    def __init__(self, suit, rank, points):
        self.suit = suit
        self.rank = rank
        # self.picture = picture
        self.points = points

    def __str__(self):
        message = self.picture
        return message


class Deck:

    def __init__(self):
        self.cards = self._generate_deck()
        shuffle(self.cards)

    def _generate_deck(self):
        cards = []
        for suit, rank in product(SUITS, RANKS.keys()):
            points = RANKS[rank]
            # picture = './Cards/'+rank+'_'+'Spades.png'
            c = Card(suit=suit, rank=rank, points=points)
            cards.append(c)
        return cards
    
    def get_card(self):
        return self.cards.pop()
    
    def __len__(self):
        return len(self.cards)