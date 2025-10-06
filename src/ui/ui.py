# src/ui/ui.py

import os

# ===== Handles basic terminal UI tasks for the game =====
class UIManager:
    def __init__(self):
        """
        Initialize the UI manager.
        Provides a separator and basic screen operations.
        """
        self.separator = "-" * 40

    # ----- Clear the terminal screen -----
    def clear_screen(self):
        """Clear the console screen."""
        os.system('cls' if os.name == 'nt' else 'clear')

    # ----- Print a separator line -----
    def print_separator(self):
        """Print a horizontal separator for clarity in menus."""
        print(f"\n{self.separator}\n")

    # ----- Display menu and get player choice -----
    def get_player_action(self, actions: list[str]) -> str:
        """
        Show available actions to the player and get input.
        Validates input and returns the selected action.
        """
        while True:
            print("\nAvailable actions:")
            for i, act in enumerate(actions, start=1):
                print(f"{i}. {act.capitalize()}")

            choice = input("Choose action: ").strip().lower()

            if choice.isdigit():
                idx = int(choice) - 1
                if 0 <= idx < len(actions):
                    return actions[idx]
            elif choice in actions:
                return choice
            print("Invalid choice! Try again.")
