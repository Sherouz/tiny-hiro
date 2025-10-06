# src/setup.py

from src.character import Hero, Enemy
from src.weapon import fists, iron_sword, short_bow

# ===== Prepares hero and enemies for the game =====
class GameSetup:
    def __init__(self):
        """
        Initialize the game setup.
        Holds references to the hero and all enemies.
        """
        self.hero = None
        self.enemies = []

    # ----- Create the hero -----
    def create_hero(self, ui=None):
        """
        Create the player's hero with default health.
        Prompts the player to equip a starting weapon.
        """
        self.hero = Hero("Hero", 100, ui=ui)
        self.hero.equip()  # choose starting weapon
        return self.hero

    # ----- Create the enemy list -----
    def create_enemies(self):
        """
        Generate a list of enemies for the game.
        Each enemy has a name, health, and weapon.
        """
        self.enemies = [
            Enemy("Goblin", 50, fists),
            Enemy("Orc", 80, iron_sword),
            Enemy("Archer", 60, short_bow)
        ]
        return self.enemies
