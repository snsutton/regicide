import pygame

from card import Card
from button import Button


class InputHandler:

    def __init__(self, card_renderer):
        self.renderer = card_renderer
        # Keep track of clicked card
        self.selected_button = None
        # Store which cards are being hovered
        self.hovered_button = None
    
    def is_point_inside_card(self, point, card_pos):
        """Check if a point (x,y) is inside a card's rectangle"""
        x, y = point
        card_x, card_y = card_pos
        
        # Get card dimensions from renderer
        width = self.renderer.CARD_WIDTH
        height = self.renderer.CARD_HEIGHT
        
        # Check if point is within card boundaries
        return (card_x <= x <= card_x + width and 
                card_y <= y <= card_y + height)
    
    def handle_mouse_event(self, event, buttons):
        mouse_pos = pygame.mouse.get_pos()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Check each card for clicks
            for button in buttons:
                if isinstance(button, Card):
                    button_pos = self.renderer.get_card_position(button)
                    if self.is_point_inside_card(mouse_pos, button_pos):
                        self.selected_button = button
                        return {'type': 'card_clicked', 
                            'card': button, 
                            'position': mouse_pos}
                elif isinstance(button, Button):
                    button_pos = button.pos()
                    if self.is_point_inside_card(mouse_pos, button_pos):
                        self.selected_button = button
                        return {'type': 'button_clicked', 
                            'button': button, 
                            'position': mouse_pos}
            
            # If we get here, no card was clicked
            self.selected_button = None
            return {'type': 'background_clicked', 
                   'position': mouse_pos}
            
        elif event.type == pygame.MOUSEBUTTONUP:
            # Handle card release
            if self.selected_button:
                old_card = self.selected_button
                self.selected_button = None
                return {'type': 'card_released', 
                       'card': old_card, 
                       'position': mouse_pos}
                
        elif event.type == pygame.MOUSEMOTION:
            # Check for hovering over cards
            for button in buttons:
                if isinstance(button, Card):
                    button_pos = self.renderer.get_card_position(button)
                    if self.is_point_inside_card(mouse_pos, button_pos):
                        if self.hovered_button != button:
                            self.hovered_button = button
                            return {'type': 'card_hover_start', 
                                'card': button, 
                                'position': mouse_pos}
                        break
                if isinstance(button, Button):
                    button_pos = button.pos()
                    if self.is_point_inside_card(mouse_pos, button_pos):
                        if self.hovered_button != button:
                            self.hovered_button = button
                            return {'type': 'button_hover_start', 
                                'button': button, 
                                'position': mouse_pos}
                        break
            else:  # No card being hovered
                if self.hovered_button:
                    old_card = self.hovered_button
                    self.hovered_button = None
                    return {'type': 'card_hover_end', 
                           'card': old_card, 
                           'position': mouse_pos}
        
        return None
