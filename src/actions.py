# src/actions.py

import random

# ===== Handles all actions a hero can perform =====
class HeroActions:
    def __init__(self, hero, ui):
        self.hero = hero
        self.ui = ui
        self.heal_limit = 3
        self.strong_limit = 2

    # ----- Normal attack -----
    def attack(self, enemy):
        damage, crit = self.hero.attack(enemy)
        if crit:
            self.ui.show_critical_hit()
        self.ui.show_message(
            f"{self.hero.name} dealt {damage} damage!",
            style="bold red" if crit else "green",
            emoji="💥" if crit else "⚔️"
        )

    # ----- Strong attack -----
    def strong_attack(self, enemy):
        if self.strong_limit <= 0:
            self.ui.show_message("No Strong Attacks left!", style="yellow", emoji="⚠️")
            return

        self.strong_limit -= 1
        
        if random.random() < 0.3:
            self.ui.show_attack_animation(self.hero.weapon.weapon_type, missed=True)
            self.ui.show_message("Strong attack missed!", style="yellow", emoji="💨")
        else:
            damage = self.hero.weapon.damage * 2
            enemy.health -= damage
            enemy.health = max(enemy.health, 0)
            
            if random.random() < 0.5:
                self.ui.show_critical_hit()
                
            self.ui.show_message(
                f"{self.hero.name} dealt {damage} strong damage! ({self.strong_limit} left)",
                style="bold red",
                emoji="💥"
            )

    # ----- Heal hero -----
    def heal(self):
        if self.heal_limit <= 0:
            self.ui.show_message("No Heals left!", style="yellow", emoji="⚠️")
            return

        self.heal_limit -= 1
        self.hero.health = min(self.hero.health + 20, self.hero.health_max)
        self.ui.show_message(f"{self.hero.name} healed 20 HP! ({self.heal_limit} left)", style="bold green", emoji="💚")

    # ----- Equip a weapon -----
    def equip(self, weapon=None):
        self.hero.equip(weapon)
        if weapon:
            self.ui.show_message(f"Equipped {weapon.name}!", style="cyan", emoji="⚔️")

    # ----- Drop current weapon -----
    def drop(self):
        old_weapon = self.hero.weapon.name
        self.hero.drop()
        if old_weapon != self.hero.weapon.name:
            self.ui.show_message(f"Dropped {old_weapon}!", style="yellow", emoji="📦")

    # ----- Handle action by name -----
    def handle(self, action: str, enemy):
        match action:
            case "attack": self.attack(enemy)
            case "strong": self.strong_attack(enemy)
            case "heal": self.heal()
            case "equip": self.equip()
            case "drop": self.drop()
            case "quit":
                self.ui.show_message("Quitting the game...", style="bold yellow", emoji="👋")
                exit()


# ===== Handles basic enemy behavior =====
class EnemyActions:
    def __init__(self, enemy):
        """
        Manage simple enemy actions.
        Currently supports attacking the hero.
        """
        self.enemy = enemy

    # ----- Enemy attack -----
    def attack(self, hero):
        """Perform a normal attack on the hero."""
        self.enemy.attack(hero)