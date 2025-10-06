# src/ui/menu.py

from rich.console import Console
from rich.table import Table

class MenuManager:
    """Handles all menu and selection functionality."""
    
    def __init__(self):
        self.console = Console()

    # ----- Choose weapon -----
    def choose_weapon(self, inventory, current_weapon_name):
        """
        Fancy menu to choose a weapon from inventory.
        Highlights currently equipped weapon.
        Returns the selected weapon or None if skipped.
        """
        while True:
            table = Table(
                title="\n🗡️ [bold cyan]Choose Your Weapon[/bold cyan]",
                padding=(0, 2),
                show_lines=True
            )
            table.add_column("#", justify="center", style="yellow", width=5, no_wrap=True)
            table.add_column("Weapon", justify="center", style="white", width=10)
            table.add_column("Damage", justify="center", style="green", width=10)
            table.add_column("Equipped", justify="center", style="magenta", width=10)

            for i, w in enumerate(inventory, start=1):
                equipped = "✅" if w.name == current_weapon_name else ""
                table.add_row(str(i), w.name, str(w.damage), equipped)

            self.console.print(table)
            choice = input("Enter weapon number to equip (Enter to skip):\n>>> ").strip()

            if not choice:
                return None
            if choice.isdigit():
                idx = int(choice) - 1
                if 0 <= idx < len(inventory):
                    return inventory[idx]

            self.console.print("[red]Invalid choice! Try again.[/red]\n")

    # ----- Player Action Menu -----
    def get_player_action(self, actions: list[str]) -> str:
        """
        Show available actions as a fancy table and return user's choice.
        """
        while True:
            table = Table(
                title="\n🎮 [bold cyan]Choose Your Action[/bold cyan]",
                padding=(0, 2),
                show_lines=True
            )
            table.add_column("#", justify="center", style="yellow", width=5, no_wrap=True)
            table.add_column("Action", justify="center", style="white", width=20)

            for i, act in enumerate(actions, start=1):
                table.add_row(str(i), act.capitalize())

            self.console.print(table)
            choice = input(">>> ").strip().lower()

            if choice.isdigit():
                idx = int(choice) - 1
                if 0 <= idx < len(actions):
                    return actions[idx]
            elif choice in actions:
                return choice

            self.console.print("[red]Invalid choice! Try again.[/red]\n")