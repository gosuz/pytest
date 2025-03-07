# had to add comment

# Make a Black Jack Game
# Player Starts with a fund of 20
# Player makes a bet and then plays with the computer(dealer)
# If player wins, wins the bet> if loses, will lose the bet. A blackjack will incur a 1.5 the reward (although I'm not sure if that is the right amount)
# Cards shouldn't be able to replicate, so it must be stored in a way so that there are no duplicates once used, until it has been shuffled.
# Objective is to win up to 100.
# It is GameOver if the player loses all their funds.

import random

# Constants
# All Caps means they are const variables.
BLACKJACK = 21  # The target value to achieve without exceeding
DEALER_STAND = 17  # The minimum value at which the dealer will stand
INITIAL_FUNDS = 20  # Starting funds for the player
BLACKJACK_PAYOUT = 1.5  # Payout multiplier for hitting a Blackjack (21 with two cards)

# Card class to represent each card in the deck
class Card:
    def __init__(self, suit, rank, value):
        # Initialize the card with its suit, rank, and value
        self.suit = suit
        self.rank = rank
        self.value = value

    def __repr__(self):
        # Represent the card as a string (e.g., "A of Spades")
        return f"{self.rank} of {self.suit}"

# Deck class to manage the deck of cards
class Deck:
    def __init__(self):
        # Create a deck of cards and shuffle it
        self.cards = self.create_deck()
        random.shuffle(self.cards)

    def create_deck(self):
        # Create a standard deck of 52 cards
        suits = ['♡', '◇', '♧', '♤']  # Four suits
        ranks = {
            '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
            '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11  # Ranks with corresponding values
        }
        # Use list comprehension to create the deck with all combinations of suits and ranks
        return [Card(suit, rank, value) for suit in suits for rank, value in ranks.items()]

    def deal_card(self):
        # Remove and return the top card from the deck
        return self.cards.pop()

    def reshuffle(self):
        # Recreate and reshuffle the deck for each round
        self.cards = self.create_deck()
        random.shuffle(self.cards)

# BlackjackGame class to handle the game logic
class BlackjackGame:
    def __init__(self):
        # Initialize the game with the player's funds and a new deck
        self.player_funds = INITIAL_FUNDS
        self.deck = Deck()

    def calculate_hand_value(self, hand):
        # Calculate the total value of a hand
        value = sum(card.value for card in hand)  # Sum the values of the cards
        aces = sum(1 for card in hand if card.rank == 'A')  # Count the number of Aces
        # Adjust value if there are Aces and the total value exceeds 21
        while value > BLACKJACK and aces:
            value -= 10  # Treat Ace as 1 instead of 11
            aces -= 1  # Decrease the count of Aces considered as 11
        return value

    def play_round(self):
        # Reshuffle the deck at the start of each round to ensure randomness
        self.deck.reshuffle()

        # Check if player has funds to continue
        if self.player_funds <= 0:
            print("Game Over! You have no funds left.")
            return False  # Stop the game

        # Get player's bet input
        bet = int(input(f"Current Fund: {self.player_funds}\nEnter your bet: "))
        if bet > self.player_funds:
            print("Insufficient funds for that bet. Try again.")
            return True  # Continue playing

        # Deal initial hands for player and dealer
        player_hand = [self.deck.deal_card(), self.deck.deal_card()]
        dealer_hand = [self.deck.deal_card(), self.deck.deal_card()]

        # Show player's hand and one of the dealer's cards
        print(f"\nDealer's hand: [{dealer_hand[0]}, ?]")  # Hide one of the dealer's cards
        print(f"Your hand: {player_hand} - Value: {self.calculate_hand_value(player_hand)}")


        # Player's turn
        while self.calculate_hand_value(player_hand) < BLACKJACK:
            # Ask player if they want to hit (draw another card) or stand (end their turn)
            action = input("Do you want to hit or stand? (h/s): ").lower()
            if action == 'h':
                # Player chooses to hit, so add a card to their hand
                player_hand.append(self.deck.deal_card())
                print(f"Your hand: {player_hand} - Value: {self.calculate_hand_value(player_hand)}")
                if self.calculate_hand_value(player_hand) > BLACKJACK:
                    # If player's hand value exceeds 21, they bust (lose)
                    print("You busted!")
                    self.player_funds -= bet
                    return True  # End round and continue the game
            else:
                # Player chooses to stand
                break

        # Dealer's turn: Dealer hits until their hand value is at least DEALER_STAND
        while self.calculate_hand_value(dealer_hand) < DEALER_STAND:
            dealer_hand.append(self.deck.deal_card())

        # Show dealer's full hand
        print(f"Dealer's hand: {dealer_hand} - Value: {self.calculate_hand_value(dealer_hand)}")

        # Determine winner by comparing hand values
        player_value = self.calculate_hand_value(player_hand)
        dealer_value = self.calculate_hand_value(dealer_hand)

        # Check for player bust
        if player_value > BLACKJACK:
            print("You lose!")
            self.player_funds -= bet
        # Check for dealer bust or player has a higher value
        elif dealer_value > BLACKJACK or player_value > dealer_value:
            winnings = bet * (BLACKJACK_PAYOUT if player_value == BLACKJACK else 1)
            self.player_funds += winnings
            print(f"You win! Your winnings: {winnings}")
        # Check for a tie
        elif player_value == dealer_value:
            print("It's a tie! Your bet is returned.")
        # Otherwise, the dealer wins
        else:
            print("You lose!")
            self.player_funds -= bet

        # Check if player has won the game by reaching 100 funds
        if self.player_funds >= 100:
            print("Congratulations! You reached 100 funds. You win the game!")
            return False  # End the game

        return True  # Continue playing

    def start_game(self):
        # Main loop to start and continue the game until the player decides to stop or runs out of funds
        playing = True
        while playing:
            playing = self.play_round()
        print("Thank you for playing Blackjack!")

# Run the game by creating an instance of the BlackjackGame class and starting it
game = BlackjackGame()
game.start_game()
