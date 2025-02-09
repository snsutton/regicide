#!/usr/bin/env python3

import pygame

from renderer import BaseRenderer
from game import Game, GameRenderer
from card import CardRenderer, CardInputHandler

def pygame_setup(g):
    pygame.init()
    screen = pygame.display.set_mode((1366, 768))
    pygame.display.set_caption("Regicide")
    
    # Create game render
    game_renderer = GameRenderer(screen)

    # Create card renderer
    card_renderer = CardRenderer(screen)

    # Create input handler
    input_handler = CardInputHandler(card_renderer)
    
    # Create some sample cards
    cards = g.players[0].hand
    cards.sort()
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Handle mouse clicks
            result = input_handler.handle_mouse_event(event, cards)
            if result:
                if result['type'] == 'card_clicked':
                    print(f"Clicked {result['card'].rank} of {result['card'].suit}")
                elif result['type'] == 'card_hover_start':
                    print(f"Hovering over {result['card'].rank} of {result['card'].suit}")
                
        # Fill background
        screen.fill((0, 100, 0))  # Green table color
        
        game_renderer.draw_game(g)

        # Draw enemy card on center of screen
        x = screen.get_width() / 2 - BaseRenderer.CARD_WIDTH / 2
        y = screen.get_height() / 2 - BaseRenderer.CARD_HEIGHT / 2
        card_renderer.draw_card(g.enemy, x, y)

        # Draw player hand
        for i, card in enumerate(cards):
            card.x = 50 + i * 120
            card.y = screen.get_height() - 200
            card_renderer.draw_card(card, card.x, card.y)
            
        pygame.display.flip()
        
    pygame.quit()


def main():
    g = Game()
    pygame_setup(g)

    return 0

if __name__ == "__main__":
    main()