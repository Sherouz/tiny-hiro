# src/weapon.py

# ===== Represents a weapon with name, type, damage, and value =====
class Weapon:
    def __init__(self, name: str, weapon_type: str, damage: int, value: int) -> None:
        """
        Create a weapon with basic stats.
        Holds the name, type, damage, and in-game value.
        """
        self.name = name
        self.weapon_type = weapon_type
        self.damage = damage
        self.value = value

    # ----- String representation -----
    def __repr__(self):
        """Return a string describing the weapon."""
        return f"Weapon(name='{self.name}', type='{self.weapon_type}', damage={self.damage}, value={self.value})"


# ===== Creates different weapons for the game =====
class WeaponFactory:
    
    # ----- Create Iron Sword -----
    def create_iron_sword(self) -> Weapon:
        """Return an Iron Sword weapon."""
        return Weapon(name="Iron Sword", weapon_type="sharp", damage=5, value=10)

    # ----- Create Short Bow -----
    def create_short_bow(self) -> Weapon:
        """Return a Short Bow weapon."""
        return Weapon(name="Short Bow", weapon_type="ranged", damage=4, value=8)

    # ----- Create Fists -----
    def create_fists(self) -> Weapon:
        """Return a basic Fists weapon."""
        return Weapon(name="Fists", weapon_type="blunt", damage=2, value=0)


# ----- Instantiate factory and weapons -----
factory = WeaponFactory()
iron_sword = factory.create_iron_sword()
short_bow = factory.create_short_bow()
fists = factory.create_fists()
