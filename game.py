import random

import deck
import card
import player

def make_standard_deck():
    d = deck.deck()

    for suit in card.card.SUITS:
        for rank in card.card.RANKS:
            d.add_card(card.card(rank, suit))

    return d

def setup_castle_deck(standard_deck):
    castle_deck = deck.deck()
    face_cards = ["K", "Q", "J"]

    for c in standard_deck.cards[:]:
        if c.rank in face_cards:
            standard_deck.remove_card(c)
            castle_deck.add_card(c)
    
    castle_deck.sort()
    castle_deck.reverse()

    for i in range(0, 3, 4):
        kings_queens_then_jacks = castle_deck.cards[i:i+4]
        random.shuffle(kings_queens_then_jacks)
        castle_deck.cards[i:i+4] = kings_queens_then_jacks

    return castle_deck

def setup_regicide():
    tavern = make_standard_deck()
    castle = setup_castle_deck(tavern)
    tavern.shuffle()

    return tavern, castle

def deal_starting_hand(tavern, player):
    for _ in range(player.MAX_HAND_SIZE):
        player.hand.add_card(tavern.draw())

class game:

    def __init__(self):
        self.player_count = 1
        self.players = [player.player(f"Player {i+1}") for i in range(self.player_count)]
        self.tavern, self.castle = setup_regicide()
        deal_starting_hand(self.tavern, self.players[0])
