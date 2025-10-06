# src/ui/display.py

from rich.console import Console
from rich.panel import Panel

class DisplayManager:
    """Handles all display-related functionality like messages and health bars."""
    
    def __init__(self):
        self.console = Console()
        self.separator = "-" * 50

    # ----- Show fancy message -----
    def show_message(self, message, style="white", emoji=None):
        """
        Display a message with color and optional emoji.
        Example:
            show_message("Critical Hit!", style="bold red", emoji="💥")
        """
        msg = f"{emoji} {message}" if emoji else message
        self.console.print(Panel(msg, style=style, border_style="bright_magenta"))

    # ----- Separator -----
    def print_separator(self):
        self.console.print(self.separator, style="bold blue")

    # ----- Health Display -----
    def draw_health(self, entity):
        """
        Draws a colored health bar for the given entity.
        Color changes with HP ratio.
        """
        hp_ratio = entity.health / entity.health_max
        if hp_ratio < 0.3:
            color = "red"
            emoji = "💀"
        elif hp_ratio < 0.6:
            color = "yellow"
            emoji = "⚠️"
        else:
            color = "green"
            emoji = "💚"

        bar_length = 20
        filled = int(hp_ratio * bar_length)
        empty = bar_length - filled

        bar = f"[{color}]" + "▮" * filled + "[/]" + "_" * empty
        hp_text = f"{emoji} [bold {color}]{entity.name}[/bold {color}] HP: {entity.health}/{entity.health_max}"
        self.console.print(Panel(f"{hp_text}\n{bar}", style=f"bold {color}", border_style=color))

    # ----- Combine healths (hero + enemy) -----
    def draw_battle_status(self, hero, enemy):
        """Draws both hero and enemy healths together for quick view."""
        self.console.print("\n[bold cyan]⚔️ Battle Status ⚔️[/bold cyan]\n")
        self.draw_health(hero)
        self.draw_health(enemy)
        self.print_separator()

    # ----- Show ASCII Art -----
    def show_ascii(self, ascii_art, color="cyan"):
        """Display ASCII art with color."""
        self.console.print(f"[{color}]{ascii_art}[/{color}]")
        