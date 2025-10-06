# src/character.py

import random
from src.weapon import fists, iron_sword, short_bow
from src.health_bar import HealthBar

# ===== Base for all characters, heroes and enemies =====
class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.health_max = health
        self.weapon = fists
    
    # ----- Perform attack on another character -----    
    def attack(self, target):
        """
        Attacks the target character using the equipped weapon.  
        Calculates damage with a 20% chance for a critical hit (double damage).  
        Reduces the target's health accordingly and updates its health bar.  
        Returns both the damage dealt and whether it was a critical hit.
        """
        crit = random.random() < 0.2  # 20% chance for critical hit
        damage = self.weapon.damage * (2 if crit else 1)
        target.health = max(target.health - damage, 0)
        target.health_bar.update()
        return damage, crit


# ===== Player-controlled character with inventory =====
class Hero(Character):
    def __init__(self, name, health, ui=None):
        super().__init__(name, health)
        self.ui = ui
        self.default_weapon = self.weapon
        self.health_bar = HealthBar(self)
        self.inventory = [fists, iron_sword, short_bow]

    # ----- Display inventory to the player -----
    def show_inventory(self):
        """
        Prints all weapons in the player's inventory with their damage values.  
        Marks the currently equipped weapon with "(equipped)".
        """
        for i, w in enumerate(self.inventory, start=1):
            equipped = "(equipped)" if w == self.weapon else ""
            print(f"{i}. {w.name} (Damage: {w.damage}) {equipped}")

    # ----- Equip a weapon from inventory -----
    def equip(self, weapon=None):
        """
        Equips a weapon from the player's inventory.  
        If a weapon is passed as an argument, equips it directly.  
        If a UI exists, allows selection through the interface.  
        Falls back to console input if no UI is available.  
        Does nothing if no valid selection is made.
        """
        if weapon:
            self.weapon = weapon
            return
        if self.ui:
            selected = self.ui.choose_weapon(self.inventory, self.weapon.name)
            if selected:
                self.weapon = selected
        else:
            # Simple fallback for when there's no UI.
            self.show_inventory()
            choice = input("\nEnter weapon number to equip (Enter to skip):\n>>> ").strip()
            if not choice:
                return
            idx = int(choice) - 1
            if 0 <= idx < len(self.inventory):
                self.weapon = self.inventory[idx]

    # ----- Drop currently equipped weapon -----
    def drop(self):
        """
        Drops the equipped weapon and switches to unarmed combat (fists).
        """
        if self.weapon == self.default_weapon:
            return
        self.weapon = self.default_weapon


# ===== Enemy Class, AI-controlled opponent =====
class Enemy(Character):
    def __init__(self, name, health, weapon):
        super().__init__(name, health)
        self.weapon = weapon
        self.health_bar = HealthBar(self)
