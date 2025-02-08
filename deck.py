import random


class Deck:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def remove_card(self, card):
        self.cards.remove(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()

    def sort(self):
        self.cards.sort()

    def reverse(self):
        self.cards.reverse()

    def __str__(self):
        return f"Deck of {len(self.cards)} cards"

    def __repr__(self):
        return f"Deck of {len(self.cards)} cards"
    
    def __len__(self):
        return len(self.cards)
