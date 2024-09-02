import random

# all caps variables are constants
INITIAL_FUNDS = 20
TARGET_FUNDS = 100
BLACKJACK = 21
DEALER_STAND = 17
BLACKJACK_PAYOUT = 1.5


# card class that represents a single card
class Card:
    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value

    # both repr and str are used to output data: repr is more for coders. str looks cleaner for end user
    def __repr__(self):
        return(f"{self.name} of {self.suit}")


# deck class to manage cards
class Deck:
    def __init__(self):
        self.cards = self.create_deck()
        random.shuffle(self.cards)

    def create_deck(self):
        suits = ['♡', '◇', '♧', '♤']
        ranks = {
            '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
            '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11
        }

        return[Card(suit, rank, value) for suit in suits for rank, value in ranks.item()]

    def deal_card(self):
        return self.cards.pop()

# main class for the blackjack game
class BlackjackGame:
    def __init__(self):
        self.player_funds = INITIAL_FUNDS
        self.deck = Deck()

    def calculate_hand_value(self, hand):
        # calculate the total value of a hand
        value = sum(card.value for card in hand)
        aces_counter = sum(1 for card in hand if card.rank == "A")
        while value > 21 and aces_counter:
            value -= 10
            aces_counter -= 1
        return value

    def play_round(self):
        # reshuffle deck before each round

        # check if player an continue
        if self.player_funds <= 0:
            print("GAME OVER")
            return False

        try:
            bet = int(input(f"Funds: {self.player_funds}. Enter Bet: "))
        except ValueError:
            print("Invalid input. Please Enter a Number.")
            return True

        if bet > self.player_funds or bet <= 0:
            print("Invalid Bet Amount")
            return True
