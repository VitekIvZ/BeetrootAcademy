import random
#from hands import Hand

SUITS = ['♠', '♣', '♦', '♥']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
POINTS = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank}{self.suit}"

    def get_points(self):
        return POINTS[self.rank]
    
    #def set_points(self, points):
    #    self.points = points

class DeckOfCards:
    def __init__(self, ranks=RANKS, suits=SUITS):
        self.deck = [Card(rank, suit) for rank in ranks for suit in suits]
        random.shuffle(self.deck)

    def draw_card(self):
        return self.deck.pop()

