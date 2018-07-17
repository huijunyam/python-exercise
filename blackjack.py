import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.rank} of {self.suit}'

class Deck:
    self.deck = []
    def __init__(self):
        for rank in ranks:
            for suit in suits:
                card = Card(suit, rank)
                self.deck.append(card)

    def __str__(self):
        deck_str = ''
        for card in self.deck:
            deck_str += f'{card.__str__()} \n'
        return deck_str

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()

class Hand:

    def __init__():
        self.total = 0
        self.cards = []
        self.aces = 0

    def add_card(card):
        self.cards.append(card)
        self.total += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def check_value():
        while self.total > 21 and self.aces:
            self.total -= 10
            self.aces -= 1
