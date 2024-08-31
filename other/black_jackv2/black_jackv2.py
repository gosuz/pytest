import random

class Card:
    def __init__(self, suit, num):
        self.suit = suit
        self.num = num

    def __str__(self):
        return(f"{self.num} of {self.suit}")


class Deck:
    def __init__(self):
        suits =  ['♡', '◇', '♧', '♤']
        nums = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.cards = [Card(suit, num) for suit in suits for num in nums]
            # This is equivalent to the following:
                # self.cards = []
                # for suit in suits:
                    # for rank in ranks:
                        # self.cards.append(Card(suit, rank))


    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()
        # bring back the last card in the 'deck'


class Player:
    def __init__(self):
        self.hand = [] # starting empty hand

    def add_card(self, card):
        self.hand.append(card)
        # add a card to the empty list

    def calculate_score(self):
        score = 0
        ace_counter = 0
        card_value = {
            '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
            'J': 10, 'Q': 10, 'K': 10, 'A': 11
        }
        # card_value determines the value of each card via using a dictionary

        for card in self.hand:
            score += card_value[card.num]
            if card.num == "A":
                ace_counter += 1

        while score > 21 and ace_counter > 0:
            score -= 10 # Change ace value to 1 instead of 11 if the hand is bust
            ace_counter -= 1

        return score

    def show_hand(self):
        card_to_strings = []
        for card in self.hand:
            card_to_string = str(card) # Convert the card to a string using the __str__ method from the Card Class
            card_to_strings.append(card_to_string) # Add the str converted card to the list

        return ", ".join(card_to_strings) # bring back a string of the list of cards in card_to_strings

    def show_first_card(self):
        if self.hand:
            return str(self.hand[0])
        return "No Cards"

class Game:
    def __init__(self):
        self.deck = Deck() # Create a new deck of cards
        self.deck.shuffle() # Shuffle the new deck
        self.player = Player() # Creates the Player
        self.dealer = Player() # Creates the Dealer

    def initial_deal(self):
        # Deals two cards for player and for dealer
        self.player.add_card(self.deck.deal_card())
        self.player.add_card(self.deck.deal_card())
        self.dealer.add_card(self.deck.deal_card())
        self.dealer.add_card(self.deck.deal_card())
        print(f"\nDealers Hand: {self.dealer.show_first_card()}")

    def player_turn(self):
        while True:
            print(f"\nPlayer's Hand: {self.player.show_hand()} (Value: {self.player.calculate_score()})")
            if self.player.calculate_score() > 21:
                print("Bust! You lose!")
                return False
            choice = input ("Hit or Stay? (h/s): ")
            if choice.lower() == 'h':
                self.player.add_card(self.deck.deal_card())
            elif choice.lower() == 's':
                break
        return True

    def dealer_turn(self):
        # reveal dealer hand when it is dealer's turns
        print(f"\nDealer's Hand: {self.dealer.show_hand()} (Value: {self.dealer.calculate_score()})")

        # dealer logic for automatic play based on score
        while self.dealer.calculate_score() < 17:
            self.dealer.add_card(self.deck.deal_card())
            print(f"\nDealer's Hand: {self.dealer.show_hand()} (Value: {self.dealer.calculate_score()})")
        if self.dealer.calculate_score() > 21:
            print("Dealer Bust! You Win!")
            return False
        return True

    def compare_scores(self):
        # compare the final scores of the player and the dealer
        player_score = self.player.calculate_score()
        dealer_score = self.dealer.calculate_score()

        if player_score > dealer_score:
            print("Player Wins!")
        elif player_score < dealer_score:
            print("Dealer Wins")
        else:
            print("It is a Tie")

    def play(self):
        # main game loop

        # Step 1: Deal Initial cards to both the player and the dealer
        self.initial_deal()

        # If the player busts, the player_turn returns False, and the game ends
        if not self.player_turn():
            return

        # If the dealer busts, the dealer_turn returns False, and the game ends
        if not self.dealer_turn():
            return

        # Otherwise compare the scores of the player and the dealer to determine the winner
        self.compare_scores()

if __name__ == "__main__":
    game = Game()
    game.play()
