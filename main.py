#!/usr/bin/env python3

import pygame

from renderer import BaseRenderer
from game import Game, GameRenderer
from card import Card, CardRenderer
from enemy import Enemy
from input_handler import InputHandler
from button import ButtonRenderer

def pygame_setup(g):
    pygame.init()
    screen = pygame.display.set_mode((1366, 768))
    pygame.display.set_caption("Regicide")
    
    # Create renderers
    game_renderer = GameRenderer(screen)
    card_renderer = CardRenderer(screen)
    button_renderer = ButtonRenderer(screen)

    # Create input handler
    input_handler = InputHandler(card_renderer)
    
    # Create some sample cards
    player_one_hand = g.players[0].hand
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Handle mouse clicks
            buttons = [card for card in player_one_hand]
            buttons.append(g.yield_button)
            result = input_handler.handle_mouse_event(event, buttons)
            if result:
                if result['type'] == 'card_clicked':
                    print(f"Clicked {result['card'].rank} of {result['card'].suit}")
                    if result['card'].rank == "A":
                        # TODO: Handle Animal cards
                        pass
                    else:
                        # Handle death by exactsies
                        damage_dealt = Card.RANK_VALUES[result['card'].rank]
                        if g.enemy.health_remaining - damage_dealt == 0:
                            g.tavern.add_card(g.enemy)
                        else:
                            g.discard.add_card(g.enemy)
                        g.enemy.health_remaining -= Card.RANK_VALUES[result['card'].rank]
                        player_one_hand.remove(result['card'])
                    
                elif result['type'] == 'card_hover_start':
                    print(f"Hovering over {result['card'].rank} of {result['card'].suit}")

                elif result['type'] == 'button_clicked':
                    print(f"Clicked {result['button'].text}")
                    if result['button'].text == "Yield":
                        print("Yield button clicked")
                        # TODO: Handle yielding

                elif result['type'] == 'button_hover_start':
                    print("Hovering over yield")

        # Handle enemy death
        if g.enemy.health_remaining <= 0:
            print("Enemy defeated!")
            g.discard.add_card(g.enemy)
            g.enemy = Enemy(g.castle.draw())
            
        
        # Fill background
        screen.fill((0, 100, 0))  # Green table color
        
        # Draw game state
        game_renderer.draw_game(g)

        # Draw Yield button
        button_renderer.draw_button(g.yield_button)

        # Draw Enemy card on center of screen
        g.enemy.x = screen.get_width() / 2 - CardRenderer.CARD_WIDTH / 2
        g.enemy.y = screen.get_height() / 2 - CardRenderer.CARD_HEIGHT / 2
        card_renderer.draw_card(g.enemy, g.enemy.x, g.enemy.y)

        # Draw player hand
        for i, card in enumerate(player_one_hand):
            # Highlight hovered/selected cards
            if card == input_handler.hovered_button:
                # TODO: Draw highlight effect here
                pass
            if card == input_handler.selected_button:
                # TODO: Draw selection effect here
                pass

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