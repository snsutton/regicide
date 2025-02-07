#!/usr/bin/env python3

import deck
import card

def standard_deck():
    d = deck.deck()
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    for suit in suits:
        for value in values:
            d.add_card(card.card(suit, value))

    return d

def deal_one(d):
    print(d)
    d.shuffle()
    print(d)
    print(d.draw())
    print(d)

    return 0

def main():
    standard = standard_deck()
    deal_one(standard)

if __name__ == "__main__":
    main()