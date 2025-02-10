import pygame


class Button:

    def __init__(self, text, x, y, width, height):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def pos(self):
        return (self.x, self.y)


class ButtonRenderer:

    def __init__(self, screen):
        self.screen = screen

    def draw_button(self, button):
        pygame.draw.rect(self.screen, (255, 255, 255), (button.x, button.y, button.width, button.height))
        font = pygame.font.SysFont('arial', 30)
        text = font.render(button.text, True, (0, 0, 0))
        text_rect = text.get_rect(center=(button.x + button.width / 2, button.y + button.height / 2))
        self.screen.blit(text, text_rect)
