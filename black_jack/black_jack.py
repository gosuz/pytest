# Make a Black Jack Game
# Player Starts with a fund of 20
# Player makes a bet and then plays with the computer(dealer)
# If player wins, wins the bet> if loses, will lose the bet. A blackjack will incur a 1.5 the reward (although I'm not sure if that is the right amount)
# Cards shouldn't be able to replicate, so it must be stored in a way so that there are no duplicates once used, until it has been shuffled.
# Objective is to win up to 100.
# It is GameOver if the player loses all their funds.

import random

# Constants
BLACKJACK = 21
DEALER_STAND = 17
INITIAL_FUNDS = 20
BLACKJACK_PAYOUT = 1.5

# Card class representing a single card
class Card:
    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value

    def __repr__(self):
        return f"{self.rank} of {self.suit}"

# Deck class representing a deck of cards
class Deck:
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = {
        '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11
    }

    def __init__(self):
        self.cards = [Card(suit, rank, value) for suit in self.suits for rank, value in self.ranks.items()]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop() if self.cards else None

# Player class representing a player
class Player:
    def __init__(self):
        self.hand = []
        self.funds = INITIAL_FUNDS
        self.current_bet = 0

    def place_bet(self, amount):
        if amount <= self.funds:
            self.current_bet = amount
            self.funds -= amount
        else:
            print("Insufficient funds.")

    def add_card(self, card):
        self.hand.append(card)

    def hand_value(self):
        value = sum(card.value for card in self.hand)
        # Adjust for Aces
        aces = sum(card.rank == 'A' for card in self.hand)
        while value > BLACKJACK and aces:
            value -= 10
            aces -= 1
        return value

    def clear_hand(self):
        self.hand = []

# Dealer class, similar to player but with different behavior
class Dealer(Player):
    def should_hit(self):
        return self.hand_value() < DEALER_STAND

# Game class to manage the flow of the game
class BlackjackGame:
    def __init__(self):
        self.deck = Deck()
        self.player = Player()
        self.dealer = Dealer()

    def play_round(self):
        # Check funds
        if self.player.funds <= 0:
            print("Game Over! You have no funds left.")
            return False

        # Get player's bet
        bet = int(input(f"You have {self.player.funds} funds. Enter your bet: "))
        self.player.place_bet(bet)

        # Deal initial cards
        self.player.add_card(self.deck.deal())
        self.dealer.add_card(self.deck.deal())
        self.player.add_card(self.deck.deal())
        self.dealer.add_card(self.deck.deal())

        # Show initial hands
        print(f"Player's Hand: {self.player.hand} - Value: {self.player.hand_value()}")
        print(f"Dealer's Hand: [{self.dealer.hand[0]}, ?]")

        # Player's turn
        while self.player.hand_value() < BLACKJACK:
            action = input("Do you want to hit or stand? (h/s): ").lower()
            if action == 'h':
                self.player.add_card(self.deck.deal())
                print(f"Player's Hand: {self.player.hand} - Value: {self.player.hand_value()}")
                if self.player.hand_value() > BLACKJACK:
                    print("You busted!")
                    break
            else:
                break

        # Dealer's turn
        if self.player.hand_value() <= BLACKJACK:
            while self.dealer.should_hit():
                self.dealer.add_card(self.deck.deal())

            print(f"Dealer's Hand: {self.dealer.hand} - Value: {self.dealer.hand_value()}")

        # Determine winner
        player_value = self.player.hand_value()
        dealer_value = self.dealer.hand_value()

        if player_value > BLACKJACK:
            print("You lose!")
        elif dealer_value > BLACKJACK or player_value > dealer_value:
            winnings = self.player.current_bet * (BLACKJACK_PAYOUT if player_value == BLACKJACK else 1)
            self.player.funds += winnings
            print(f"You win! Your winnings: {winnings}")
        elif player_value == dealer_value:
            self.player.funds += self.player.current_bet  # Return bet
            print("It's a tie!")
        else:
            print("You lose!")

        # Clear hands for next round
        self.player.clear_hand()
        self.dealer.clear_hand()

        # Reshuffle if the deck is low on cards
        if len(self.deck.cards) < 10:
            self.deck = Deck()
            print("Deck reshuffled!")

        # Check winning condition
        if self.player.funds >= 100:
            print("Congratulations! You reached 100 funds. You win the game!")
            return False

        return True

# Run the game
game = BlackjackGame()
while game.play_round():
    continue

print("Thank you for playing Blackjack!")
