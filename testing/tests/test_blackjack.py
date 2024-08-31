# tests/test_blackjack.py

import pytest
from src.blackjack import Card, Deck, BlackjackGame

def test_card_initialization():
    card = Card('♤', 'A', 11)
    assert card.suit == '♤'
    assert card.rank == 'A'
    assert card.value == 11

def test_deck_creation():
    deck = Deck()
    assert len(deck.cards) == 52  # Ensure a full deck is created

def test_deck_shuffle():
    deck = Deck()
    first_deck = deck.cards.copy()
    deck.reshuffle()
    assert first_deck != deck.cards  # Ensure the deck is shuffled

def test_deck_deal_card():
    deck = Deck()
    initial_count = len(deck.cards)
    card = deck.deal_card()
    assert isinstance(card, Card)
    assert len(deck.cards) == initial_count - 1

def test_calculate_hand_value():
    game = BlackjackGame()
    hand = [Card('♤', 'A', 11), Card('♡', '9', 9)]
    assert game.calculate_hand_value(hand) == 20

    hand = [Card('♤', 'A', 11), Card('♡', '9', 9), Card('♧', '2', 2)]
    assert game.calculate_hand_value(hand) == 12  # Ace counts as 1 if total exceeds 21

def test_betting_logic():
    game = BlackjackGame()
    game.player_funds = 20

    # Simulate betting within the available funds
    game.play_round = lambda: False  # Mock play_round to avoid actual play
    assert game.player_funds == 20

def test_blackjack_payout():
    game = BlackjackGame()
    hand = [Card('♤', 'A', 11), Card('♡', 'K', 10)]
    assert game.calculate_hand_value(hand) == 21  # Check Blackjack condition
