import pygame

class BaseRenderer:

    def __init__(self, screen):
        self.screen = screen
    
        # Define colors
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        
        # Card dimensions
        self.CARD_WIDTH = 100
        self.CARD_HEIGHT = 140
        self.CORNER_RADIUS = 10
        
        # Symbol mappings
        self.SUIT_SYMBOLS = {
            'Hearts': '♥',
            'Diamonds': '♦',
            'Clubs': '♣',
            'Spades': '♠'
        }
        
        # Initialize fonts
        pygame.font.init()
        self.font = pygame.font.SysFont('arial', 30)
        self.small_font = pygame.font.SysFont('arial', 20)

    def draw_rounded_rect(self, surface, rect, color, radius=10):
        """Draw a rounded rectangle"""
        pygame.draw.rect(surface, color, rect, border_radius=radius)