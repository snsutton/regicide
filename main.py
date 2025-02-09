#!/usr/bin/env python3

import pygame

from game import Game, GameRenderer
from card import CardRenderer

def pygame_setup(g):
    pygame.init()
    screen = pygame.display.set_mode((1366, 768))
    pygame.display.set_caption("Regicide")
    
    # Create game render
    game_renderer = GameRenderer(screen)

    # Create card renderer
    card_renderer = CardRenderer(screen)
    
    # Create some sample cards
    cards = g.players[0].hand
    cards.sort()
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        # Fill background
        screen.fill((0, 100, 0))  # Green table color
        
        game_renderer.draw_game(g)
        card_renderer.draw_card(g.enemy, 50 + 4 * 120, 50)

        # Draw cards in a row
        for i, card in enumerate(cards):
            card_renderer.draw_card(card, 50 + i * 120, 200)
            
        pygame.display.flip()
        
    pygame.quit()


def main():
    g = Game()
    pygame_setup(g)

    return 0

if __name__ == "__main__":
    main()