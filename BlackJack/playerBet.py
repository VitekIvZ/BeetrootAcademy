class Bet:
    def __init__(self, balance=100):
        self.balance = balance
        self.current_bet = 0

    def place_bet(self, amount):
        if amount > self.balance:
            print("You don't have enough balance to place this bet.")
            return False
        self.current_bet = amount
        self.balance -= amount
        return True

    def win_bet(self):
        self.balance += self.current_bet * 2
        self.current_bet = 0

    def lose_bet(self):
        self.current_bet = 0

    def surrender_bet(self):
        self.balance += self.current_bet // 2
        self.current_bet = 0
