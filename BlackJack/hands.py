from cards import DeckOfCards
from cards import Card

class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def get_points(self):
        total_points = 0
        aces = 0
        for card in self.cards:
            points = card.get_points()
            if isinstance(points, list):
                aces += 1
                points = 11
            total_points += points

        while total_points > 21 and aces:
            total_points -= 10
            aces -= 1

        return total_points
    
    def has_blackjack(self):
        return (
        len(self.cards) == 2 and 
        self.get_points() == 21 and 
        any(card.rank == 'A' for card in self.cards)
        )
    
    def clear(self):
        self.cards = []

    def __str__(self):
        return ', '.join(str(card) for card in self.cards)
