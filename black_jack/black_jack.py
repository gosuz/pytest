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

# Function to create a deck of cards
def create_deck():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = {
        '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11
    }
    deck = [{'suit': suit, 'rank': rank, 'value': value} for suit in suits for rank, value in ranks.items()]
    random.shuffle(deck)
    return deck

# Function to calculate the value of a hand
def calculate_hand_value(hand):
    value = sum(card['value'] for card in hand)
    aces = sum(1 for card in hand if card['rank'] == 'A')
    while value > BLACKJACK and aces:
        value -= 10
        aces -= 1
    return value

# Function to deal a card from the deck
def deal_card(deck):
    return deck.pop()

# Function to play a round of Blackjack
def play_round(player_funds, deck):
    # Check if player has funds
    if player_funds <= 0:
        print("Game Over! You have no funds left.")
        return player_funds, False

    # Get player's bet
    bet = int(input(f"You have {player_funds} funds. Enter your bet: "))
    if bet > player_funds:
        print("Insufficient funds for that bet. Try again.")
        return player_funds, True

    # Initial hands
    player_hand = [deal_card(deck), deal_card(deck)]
    dealer_hand = [deal_card(deck), deal_card(deck)]

    # Show initial hands
    print(f"Your hand: {player_hand} - Value: {calculate_hand_value(player_hand)}")
    print(f"Dealer's hand: [{dealer_hand[0]}, ?]")

    # Player's turn
    while calculate_hand_value(player_hand) < BLACKJACK:
        action = input("Do you want to hit or stand? (h/s): ").lower()
        if action == 'h':
            player_hand.append(deal_card(deck))
            print(f"Your hand: {player_hand} - Value: {calculate_hand_value(player_hand)}")
            if calculate_hand_value(player_hand) > BLACKJACK:
                print("You busted!")
                player_funds -= bet
                return player_funds, True
        else:
            break

    # Dealer's turn
    while calculate_hand_value(dealer_hand) < DEALER_STAND:
        dealer_hand.append(deal_card(deck))

    print(f"Dealer's hand: {dealer_hand} - Value: {calculate_hand_value(dealer_hand)}")

    # Determine winner
    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)

    if player_value > BLACKJACK:
        print("You lose!")
        player_funds -= bet
    elif dealer_value > BLACKJACK or player_value > dealer_value:
        winnings = bet * (BLACKJACK_PAYOUT if player_value == BLACKJACK else 1)
        player_funds += winnings
        print(f"You win! Your winnings: {winnings}")
    elif player_value == dealer_value:
        print("It's a tie! Your bet is returned.")
    else:
        print("You lose!")
        player_funds -= bet

    # Reshuffle if the deck is low on cards
    if len(deck) < 10:
        deck = create_deck()
        print("Deck reshuffled!")

    # Check winning condition
    if player_funds >= 100:
        print("Congratulations! You reached 100 funds. You win the game!")
        return player_funds, False

    return player_funds, True

# Main function to run the game
def main():
    player_funds = INITIAL_FUNDS
    deck = create_deck()
    playing = True

    while playing:
        player_funds, playing = play_round(player_funds, deck)

    print("Thank you for playing Blackjack!")

# Run the game
main()
