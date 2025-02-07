#!/usr/bin/env python3

import pprint
import random

import deck
import card
import player

def make_standard_deck():
    d = deck.deck()

    for suit in card.card.SUITS:
        for rank in card.card.RANKS:
            d.add_card(card.card(suit, rank))

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

    player_one = player.player("Player One")
    player_one.hand = [tavern.draw() for _ in range(player.player.MAX_HAND_SIZE)]
    
    print(f"{player_one.name} has:")
    pprint.pprint(player_one.hand)

    pass

def main():
    setup_regicide()

if __name__ == "__main__":
    main()