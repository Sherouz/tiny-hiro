# cli.py

from src.ui.fancy_ui import FancyUIManager
from src.setup import GameSetup
from src.battle import BattleManager

# ===== Controls the flow of the Tiny Hero game =====
class GameController:
    def __init__(self):
        self.ui = FancyUIManager()
        self.setup = GameSetup()

    # ----- Main game loop -----
    def run_tiny_hero(self):
        # Show animated intro
        self.ui.show_intro()
        
        hero = self.setup.create_hero(ui=self.ui)
        enemies = self.setup.create_enemies()

        for enemy in enemies:
            battle = BattleManager(hero, self.ui)
            battle.start(enemy)

        # Show victory screen
        self.ui.show_victory()
        self.ui.show_message("All enemies defeated! You are the champion! 🏆", style="bold green", emoji="🎉")


# ----- Wrapper to run the game -----
def run_tiny_hero_wrapper():
    controller = GameController()
    controller.run_tiny_hero()