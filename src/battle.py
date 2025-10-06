# src/battle.py

import random
from src.actions import HeroActions

class BattleManager:
    def __init__(self, hero, ui_manager):
        self.hero = hero
        self.ui = ui_manager
        self.actions_list = ["attack", "strong", "heal", "equip", "drop", "quit"]
        self.hero_actions = HeroActions(hero, self.ui)

    def determine_initiative(self, enemy):
        return (self.hero, enemy) if random.random() < 0.5 else (enemy, self.hero)

    def take_turn(self, actor, target):
        if actor == self.hero:
            action = self.ui.get_player_action(self.actions_list)
            self.hero_actions.handle(action, target)
        else:
            damage, crit = actor.attack(target)
            if crit:
                self.ui.show_critical_hit()
            self.ui.show_message(
                f"{actor.name} dealt {damage} damage to {target.name}!",
                style="bold red" if crit else "red",
                emoji="💥" if crit else "⚔️"
            )
            
    # ----- Start the battle loop -----
    def start(self, enemy):
        # Show battle start screen with enemy art
        self.ui.show_battle_start(enemy.name)
        self.ui.show_enemy_art(enemy.name)
        input("\n[Press Enter to begin battle...]")
        
        while self.hero.health > 0 and enemy.health > 0:
            self.ui.clear_screen()
            self.ui.draw_battle_status(self.hero, enemy)

            first, second = self.determine_initiative(enemy)
            
            # Hero's turn
            if first == self.hero:
                action = self.ui.get_player_action(self.actions_list)
                
                # Show attack animation if attacking
                if action in ["attack", "strong"]:
                    self.ui.show_attack_animation(self.hero.weapon.weapon_type)
                
                self.hero_actions.handle(action, second)
                
                # Enemy's turn if still alive
                if second.health > 0:
                    self.ui.show_enemy_attack_animation()
                    damage, crit = second.attack(first)
                    if crit:
                        self.ui.show_critical_hit()
                    self.ui.show_message(
                        f"{second.name} dealt {damage} damage to {first.name}!",
                        style="bold red" if crit else "red",
                        emoji="💥" if crit else "⚔️"
                    )
            else:
                # Enemy attacks first
                self.ui.show_enemy_attack_animation()
                damage, crit = first.attack(second)
                if crit:
                    self.ui.show_critical_hit()
                self.ui.show_message(
                    f"{first.name} dealt {damage} damage to {second.name}!",
                    style="bold red" if crit else "red",
                    emoji="💥" if crit else "⚔️"
                )
                
                # Hero's turn if still alive
                if second.health > 0:
                    action = self.ui.get_player_action(self.actions_list)
                    
                    if action in ["attack", "strong"]:
                        self.ui.show_attack_animation(self.hero.weapon.weapon_type)
                    
                    self.hero_actions.handle(action, first)

            # Show updated health bars after each round
            self.ui.draw_battle_status(self.hero, enemy)
            input("\nPress Enter to continue...")

        # End of battle
        if self.hero.health <= 0:
            self.ui.show_game_over()
            exit()
        else:
            self.ui.show_message(f"{enemy.name} defeated!", style="bold green", emoji="🏆")
            input("Press Enter to continue...")
            