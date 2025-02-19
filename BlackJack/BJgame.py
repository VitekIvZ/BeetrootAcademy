from cards import DeckOfCards
from cards import Card
from hands import Hand
from playerBet import Bet
from players import Player

class BlackJackGame:
    def __init__(self):
        self.deck = DeckOfCards()
        self.player = None
        self.dealer = Player("Dealer")

    def start_game(self):
        player_name = input("Enter your name: ")
        self.player = Player(player_name)
        print(f"Welcome to BlackJack, {self.player.name}!")
        
        while True:
            self._play_round()
            if self.player.bet.balance == 0:
                print("You have run out of balance. Game over.")
                return     
            elif input("Do you want to play another round? (y/n): ").lower() != 'y':
                print("Thank you for playing! Goodbye.")
                return
            
    def _play_round(self):       
        print(f"Your current balance is: {self.player.bet.balance}")
        self._place_bet()
        self._deal_initial_cards()
        self._show_initial_hands()
        
        self._handle_dealer_ace()
        
        self._handle_ace_choice(self.player.hand)
            
        if self._check_blackjack():
            return

        self._player_turn()
        if self.player.hand.get_points() > 21:
            return

        self._dealer_turn()
        self._determine_winner()
        
        self.player.hand.clear()
        self.dealer.hand.clear()
        
        self.deck = DeckOfCards()
            
    def _place_bet(self):
        while True:
            try:
                bet_amount = int(input("Place your bet: "))
                if self.player.place_bet(bet_amount):
                    break
            except ValueError:
                print("Invalid input. Please enter a number.")       
    
    def _deal_initial_cards(self):
        for _ in range(2):
            self.player.hand.add_card(self.deck.draw_card())
            self.dealer.hand.add_card(self.deck.draw_card())
    
    def _show_initial_hands(self):
        print(f"Dealer's hand: {self.dealer.hand.cards[0]}, ?")
        print(f"Your hand: {self.player.hand} (Points: {self.player.hand.get_points()})")   
        
    def _check_blackjack(self):
        if self.player.hand.has_blackjack():
            print("Blackjack! You win!")
            self.player.win_bet()
            return True
        elif self.dealer.hand.has_blackjack():
            print(f"Dealer's hand: {self.dealer.hand} (Points: {self.dealer.hand.get_points()})")
            print("Dealer has Blackjack! Dealer wins!")
            self.player.lose_bet()
            return True
        return False    
    
    def _player_turn(self):
        while True:
            action = input("Do you want to [h]it, [s]tand, or su[r]render? ").lower()
            if action == 'h':
                self.player.hand.add_card(self.deck.draw_card())
                print(f"Your hand: {self.player.hand} (Points: {self.player.hand.get_points()})")
                self._handle_ace_choice(self.player.hand)
                if self.player.hand.get_points() > 21:
                    print("You busted! Dealer wins.")
                    self.player.lose_bet()
                    return
            elif action == 's':
                break
            elif action == 'r':
                print("You have chosen to surrender. You lose half your bet.")
                self.player.surrender_bet()
                return
            else:
                print("Invalid choice. Please enter 'h', 's', or 'r'.")  
                
    def _dealer_turn(self):
        print(f"Dealer's hand: {self.dealer.hand} (Points: {self.dealer.hand.get_points()})")
        while self.dealer.hand.get_points() < 17:
            self.dealer.hand.add_card(self.deck.draw_card())
            print(f"Dealer's hand: {self.dealer.hand} (Points: {self.dealer.hand.get_points()})")

    def _determine_winner(self):
        player_points = self.player.hand.get_points()
        dealer_points = self.dealer.hand.get_points()

        if dealer_points > 21 or player_points > dealer_points:
            print("You win!")
            self.player.win_bet()
        elif player_points <= dealer_points:
            print("Dealer wins!")
            self.player.lose_bet()

        print(f"Your current balance is: {self.player.bet.balance}")

    def _handle_ace_choice(self, hand):
        for card in hand.cards:
            if card.rank == 'A' and card.points == 11:
                while True:
                    choice = input("You have an Ace! Do you want it to be worth 1 or 11 points? (1/11): ")
                    if choice == '1':
                        card.set_points(1)
                        break
                    elif choice == '11':
                        card.set_points(11)
                        break
                    else:
                        print("Invalid choice. Please enter 1 or 11.")
                        
    def _handle_dealer_ace(self):
        for card in self.dealer.hand.cards:
            if card.rank == 'A':
                card.set_points(11)

if __name__ == "__main__":
    game = BlackJackGame()
    game.start_game()
    