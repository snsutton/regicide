import pygame

from renderer import BaseRenderer

class Card:

    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]

    SUIT_SYMBOLS = {
        "Clubs": "♣",
        "Diamonds": "♦",
        "Hearts": "♥",
        "Spades": "♠"
    }

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        r = self.rank if len(self.rank) > 1 else f"{self.rank} "
        s = self.SUIT_SYMBOLS[self.suit]

        drawing = [
            "┌─────────┐",
            f"│ {r}      │",
            f"│ {s}       │",
            f"│         │",
            f"│       {s} │",
            f"│       {r}│",
            "└─────────┘"
        ]

        return "\n".join(drawing)

    def __repr__(self):
        return f"{self.rank} of {self.suit}"

    def __lt__(self, other):
        """
        Compare cards based on rank first, then suit.
        This enables sorting with the standard sort() function.
        """
        # Get numeric values for comparison
        self_rank_val = self.RANKS.index(self.rank)
        other_rank_val = self.RANKS.index(other.rank)
        self_suit_val = self.SUITS.index(self.suit)
        other_suit_val = self.SUITS.index(other.suit)

        # Compare ranks first, then suits if ranks are equal
        if self_rank_val == other_rank_val:
            return self_suit_val < other_suit_val
        return self_rank_val < other_rank_val

    def __iter__(self):
        return iter([self.__str__()])


class CardRenderer(BaseRenderer):
        
    def draw_rounded_rect(self, surface, rect, color, radius=10):
        """Draw a rounded rectangle"""
        pygame.draw.rect(surface, color, rect, border_radius=radius)
        
    def get_card_color(self, suit):
        """Return color based on suit"""
        return self.RED if suit in ['Hearts', 'Diamonds'] else self.BLACK
    
    def draw_card(self, card, x, y):
        """Draw a single card at the specified position"""
        # Draw card background
        card_rect = pygame.Rect(x, y, self.CARD_WIDTH, self.CARD_HEIGHT)
        self.draw_rounded_rect(self.screen, card_rect, self.WHITE)
        pygame.draw.rect(self.screen, self.BLACK, card_rect, 2, border_radius=self.CORNER_RADIUS)
        
        # Get card color based on suit
        card_color = self.get_card_color(card.suit)
        
        # Draw card rank and suit in top left
        rank_text = self.font.render(str(card.rank), True, card_color)
        suit_text = self.font.render(self.SUIT_SYMBOLS[card.suit], True, card_color)
        
        # Position text
        self.screen.blit(rank_text, (x + 5, y + 5))
        self.screen.blit(suit_text, (x + 5, y + 35))
        
        # Draw center suit symbol
        center_symbol = self.font.render(self.SUIT_SYMBOLS[card.suit], True, card_color)
        symbol_x = x + (self.CARD_WIDTH - center_symbol.get_width()) // 2
        symbol_y = y + (self.CARD_HEIGHT - center_symbol.get_height()) // 2
        self.screen.blit(center_symbol, (symbol_x, symbol_y))
        
        # Draw bottom right rank and suit (inverted)
        bottom_rank = pygame.transform.rotate(rank_text, 180)
        bottom_suit = pygame.transform.rotate(suit_text, 180)

        if card.rank == '10':
            self.screen.blit(bottom_rank, (x + self.CARD_WIDTH - 35, y + self.CARD_HEIGHT - 40))
        else:
            self.screen.blit(bottom_rank, (x + self.CARD_WIDTH - 25, y + self.CARD_HEIGHT - 40))

        self.screen.blit(bottom_suit, (x + self.CARD_WIDTH - 25, y + self.CARD_HEIGHT - 70))
