# src/ui/animations.py

import time
import os
from rich.console import Console
from src.ui.ascii_arts import *

class AnimationManager:
    """Handles all animations and intro sequences."""
    
    def __init__(self):
        self.console = Console()

    # ----- Clear screen -----
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    # ----- Show ASCII with color -----
    def show_ascii(self, ascii_art, color="cyan"):
        """Display ASCII art with color."""
        self.console.print(f"[{color}]{ascii_art}[/{color}]")

    # ----- Show Intro with Animation -----
    def show_intro(self):
        """Display animated intro sequence."""
        
        # Show title
        self.clear_screen()
        self.show_ascii(TITLE_BANNER, "bright_cyan")
        time.sleep(1.5)
        
        # Wait for user
        self.console.print("\n[bold yellow]Press Enter to begin your quest...[/bold yellow]", justify="center")
        input()
        
        # Show intro text
        self.clear_screen()
        self.show_ascii(INTRO_TEXT, "bright_magenta")
        time.sleep(5)
        
        # Show loading animation
        self._show_loading_bar()
        
        # Show weapon icons
        self.console.print("\n         🗡️  ⚡  🛡️  💎  🏹\n", justify="center")
        time.sleep(1)
        
        self.console.print("\n[bold green]✨ Ready! Let's begin! ✨[/bold green]\n", justify="center")
        time.sleep(1)

    # ----- Loading Bar Animation -----
    def _show_loading_bar(self):
        """Display animated loading progress bar."""
        progress_steps = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        
        for i in progress_steps:
            self.clear_screen()
            self.console.print("\n[bold cyan]⚔️ PREPARING YOUR ADVENTURE ⚔️[/bold cyan]\n", justify="center")
            
            bar_length = 30
            filled = int((i / 100) * bar_length)
            empty = bar_length - filled
            bar = "█" * filled + "░" * empty
            
            self.console.print(f"    [{bar}] {i}%", style="bright_green", justify="center")
            time.sleep(0.5)
        
        time.sleep(0.5)

    # ----- Show Battle Start -----
    def show_battle_start(self, enemy_name):
        """Display battle start animation."""
        self.clear_screen()
        self.show_ascii(BATTLE_START, "red")
        self.console.print(f"\n[bold red]⚔️  A wild {enemy_name} appears!  ⚔️[/bold red]\n")

    # ----- Show Enemy ASCII -----
    def show_enemy_art(self, enemy_name):
        """Display ASCII art for specific enemy."""
        enemy_art = {
            "Goblin": GOBLIN,
            "Orc": ORC,
            "Archer": ARCHER,
            "Dragon": DRAGON
        }
        art = enemy_art.get(enemy_name, GOBLIN)
        self.show_ascii(art, "red")

    # ----- Show Critical Hit -----
    def show_critical_hit(self):
        """Display critical hit effect."""
        self.show_ascii(CRITICAL_HIT, "yellow")

    # ----- Show Attack Animation -----
    def show_attack_animation(self, weapon_type, missed=False):
        """Display attack animation based on weapon type."""
        if missed:
            self.show_ascii(ATTACK_MISS, "yellow")
            time.sleep(0.5)
            return
        
        animations = {
            "sharp": ATTACK_SWORD,
            "ranged": ATTACK_BOW,
            "blunt": ATTACK_PUNCH
        }
        
        animation = animations.get(weapon_type, ATTACK_PUNCH)
        self.show_ascii(animation, "cyan")
        time.sleep(0.5)

    # ----- Show Enemy Attack Animation -----
    def show_enemy_attack_animation(self):
        """Display enemy attack animation."""
        self.show_ascii(ENEMY_ATTACK, "red")
        time.sleep(0.5)

    # ----- Show Game Over -----
    def show_game_over(self):
        """Display game over screen."""
        self.clear_screen()
        self.show_ascii(GAME_OVER, "red")
        input("\n[Press Enter to exit...]")

    # ----- Show Victory -----
    def show_victory(self):
        """Display victory screen."""
        self.clear_screen()
        self.show_ascii(VICTORY_BANNER, "green")
        input("\n[Press Enter to continue...]")