# src/ui/fancy_ui.py

"""
Main UI Manager - Combines all UI modules into one interface.
Uses composition to delegate functionality to specialized managers.
"""

import os
from src.ui.display import DisplayManager
from src.ui.menu import MenuManager
from src.ui.animations import AnimationManager

class FancyUIManager:
    """
    Main UI system that combines display, menu, and animation functionality.
    Acts as a facade pattern for easier access to all UI features.
    """
    
    def __init__(self):
        # Composition: Delegate to specialized managers
        self.display = DisplayManager()
        self.menu = MenuManager()
        self.animations = AnimationManager()
    
    
    # ========== Screen Management ==========
    def clear_screen(self):
        """Clear the terminal screen."""
        os.system('cls' if os.name == 'nt' else 'clear')
    

    # ========== Display Methods (Delegated) ==========
    def show_message(self, message, style="white", emoji=None):
        """Display a styled message with optional emoji."""
        self.display.show_message(message, style, emoji)
    
    def print_separator(self):
        """Print a separator line."""
        self.display.print_separator()
    
    def draw_health(self, entity):
        """Draw health bar for an entity."""
        self.display.draw_health(entity)
    
    def draw_battle_status(self, hero, enemy):
        """Draw battle status showing both hero and enemy health."""
        self.display.draw_battle_status(hero, enemy)
    
    def show_ascii(self, ascii_art, color="cyan"):
        """Display ASCII art with color."""
        self.display.show_ascii(ascii_art, color)
    

    # ========== Menu Methods (Delegated) ==========
    def choose_weapon(self, inventory, current_weapon_name):
        """Show weapon selection menu."""
        return self.menu.choose_weapon(inventory, current_weapon_name)
    
    def get_player_action(self, actions: list[str]) -> str:
        """Show action menu and get player choice."""
        return self.menu.get_player_action(actions)
    

    # ========== Animation Methods (Delegated) ==========
    def show_intro(self):
        """Display the game intro animation."""
        self.animations.show_intro()
    
    def show_battle_start(self, enemy_name):
        """Display battle start animation."""
        self.animations.show_battle_start(enemy_name)
    
    def show_enemy_art(self, enemy_name):
        """Display enemy ASCII art."""
        self.animations.show_enemy_art(enemy_name)
    
    def show_critical_hit(self):
        """Display critical hit animation."""
        self.animations.show_critical_hit()
    
    def show_attack_animation(self, weapon_type, missed=False):
        """Display attack animation."""
        self.animations.show_attack_animation(weapon_type, missed)
    
    def show_enemy_attack_animation(self):
        """Display enemy attack animation."""
        self.animations.show_enemy_attack_animation()
    
    def show_game_over(self):
        """Display game over screen."""
        self.animations.show_game_over()
    
    def show_victory(self):
        """Display victory screen."""
        self.animations.show_victory()
