import random

import deck
import card
import player
import enemy


class Game:

    def __init__(self):
        self.player_count = 1
        self.players = [player.Player(
            f"Player {i+1}") for i in range(self.player_count)]
        self.current_player = self.players[0]
        
        self.tavern = self.make_standard_deck()
        self.castle = self.make_castle_deck()
        self.tavern.shuffle()
        
        self.deal_starting_hand(self.players[0])

        self.enemy = enemy.Enemy(self.castle.draw())

    def make_standard_deck(self):
        d = deck.Deck()

        for suit in card.Card.SUITS:
            for rank in card.Card.RANKS:
                d.add_card(card.Card(rank, suit))

        return d

    def make_castle_deck(self):
        castle_deck = deck.Deck()
        face_cards = ["K", "Q", "J"]

        for c in self.tavern.cards[:]:
            if c.rank in face_cards:
                self.tavern.remove_card(c)
                castle_deck.add_card(c)

        castle_deck.sort()
        castle_deck.reverse()

        for i in range(0, 3, 4):
            kings_queens_then_jacks = castle_deck.cards[i:i+4]
            random.shuffle(kings_queens_then_jacks)
            castle_deck.cards[i:i+4] = kings_queens_then_jacks

        return castle_deck

    def deal_starting_hand(self, next_player):
        for _ in range(next_player.MAX_HAND_SIZE):
            next_player.hand.add_card(self.tavern.draw())

    def __str__(self):
        game_state = []
        
        game_state.append(f"Tavern: {len(self.tavern)}")
        game_state.append(f"Castle: {len(self.castle)}")
        game_state.append(self.enemy.__str__())
        game_state.append(self.current_player.__str__())

        return "\n".join(game_state)
