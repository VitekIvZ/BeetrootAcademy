#from cards import DeckOfCards
from hands import Hand
from playerBet import Bet

class Player:
    def __init__(self, name, balance=100):
        self.name = name
        self.hand = Hand()
        self.bet = Bet(balance)

    def place_bet(self, amount):
        return self.bet.place_bet(amount)

    def win_bet(self):
        self.bet.win_bet()

    def lose_bet(self):
        self.bet.lose_bet()

    def surrender_bet(self):
        self.bet.surrender_bet()
