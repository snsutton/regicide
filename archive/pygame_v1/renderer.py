import pygame

class BaseRenderer:

    # Define colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)

    def __init__(self, screen):
        self.screen = screen
        
        # Initialize fonts
        pygame.font.init()
        self.font = pygame.font.SysFont('arial', 30)
        self.small_font = pygame.font.SysFont('arial', 20)
 