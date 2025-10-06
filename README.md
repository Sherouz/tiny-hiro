# ⚔️ Tiny Hero: A Terminal RPG Adventure 🛡️

**Tiny Hero** is a terminal-based mini RPG developed in Python that leverages the powerful **rich** library for a colorful, fancy UI with special effects. In this game, you play as a hero tasked with saving the kingdom by defeating evil enemies!

---

## 📑 Table of Contents

- [⚔️ Tiny Hero: A Terminal RPG Adventure 🛡️](#-tiny-hero-a-terminal-rpg-adventure-️)
    - [📑 Table of Contents](#-table-of-contents)
    - [🎥 Demo Video](#-demo-video)
    - [💡 Educational Purpose](#-educational-purpose)
    - [✨ Key Features](#-key-features)
    - [🚀 Installation](#-installation)
    - [🎮 Gameplay Guide](#-gameplay-guide)
    - [📁 Modular Project Structure](#-modular-project-structure)
    - [🛠️ Technologies](#-technologies)
    - [🤝🏽 Contribution](#-contribution)
    - [📃 License](#-license)
    - [🙌🏽 Acknowledgments](#-acknowledgments)

---

## 🎥 Demo Video

Watch a demo session of **Tiny Hero** in action on YouTube:

[![Watch Tiny Hero Demo](https://img.youtube.com/vi/Xje8ivBpUlI/0.jpg)](https://youtu.be/Xje8ivBpUlI)

Or click the link directly: [Watch on YouTube](https://youtu.be/Xje8ivBpUlI)

---

## 💡 Educational Purpose

This project is developed to practice and master key Python concepts and software design:

* **Object-Oriented Design (OOP):** Strong use of inheritance (`Character`, `Hero`, `Enemy`), composition, and encapsulation to model game entities.
* **Modular Code & Structured Imports:** Separation of game logic into files (`actions.py`, `battle.py`, `weapon.py`) for readability and maintainability.
* **CLI UI with Rich:** Using the `rich` library to create dynamic health bars, colorful messaging panels, and attractive menu tables.
* **Facade Pattern in UI:** Using the **`FancyUIManager`** class as a simple facade to manage all UI subsystems (animations, menus, displays).
* **Turn-Based Logic:** Implementing random initiative mechanism (`determine_initiative`) in `BattleManager`.

---

## ✨ Key Features

### Battle & Action System

* **Classic Turn-Based Combat:** Turn-based fights with random initiative.
* **Critical Hit:** 20% chance to deal double damage on normal attacks.
* **Limited Special Abilities:** Use **Strong Attack** (2x damage, 2 times per battle) and **Heal** (restore 20 HP, 3 times per battle).
* **Weapon Management:** Equip and switch weapons from inventory during combat.

### UI & Special Effects

* **Fancy UI:** Panels, tables, and highlighted colors for all interactions and messages.
* **Advanced Health Bars:** Color-coded health bars (green, yellow, red) based on HP ratio.
* **Terminal Animations:** ASCII animations for **battle start**, **attacks** (weapon-based), **enemy attacks**, **critical hits**, and **game over** screen.
* **Intro Sequence:** Animated opening with progress bar and ASCII banner.

---

## 🚀 Installation

You need Python 3 and the `rich` library to run this mini-game.

```bash
# 1. Clone the repository (or download files)
git clone [https://github.com/Sherouz/tiny-hero.git](https://github.com/YourUsername/tiny-hero.git)
cd tiny-hero

# 2. Install rich library
pip install rich

# 3. Run the game
python main.py
```

---

## 🎮 Gameplay Guide

After starting the game, choose your starting weapon. Then, face a series of enemy battles.

### Battle Action Menu

Each turn, you’ll see the following menu. Type the number or name to choose:

|   #   | Action | Description                                          | Limit        |
| :---: | :----- | :--------------------------------------------------- | :----------- |
| **1** | Attack | Normal attack with chance of Critical.               | Unlimited    |
| **2** | Strong | Stronger attack (x2 damage) with 30% chance to miss. | 2 per battle |
| **3** | Heal   | Restore 20 HP.                                       | 3 per battle |
| **4** | Equip  | Open menu to equip another weapon from inventory.    | Unlimited    |
| **5** | Drop   | Drop current weapon and use Fists.                   | Unlimited    |
| **6** | Quit   | Exit the game.                                       | –            |

### Turn Order

At the start of each round, the system randomly determines if the hero or enemy attacks first.

---

## 📁 Modular Project Structure

Designed to follow OOP principles and separate responsibilities:

| File/Module                | Main Responsibility & Design Pattern                                                            |
| :------------------------- | :---------------------------------------------------------------------------------------------- |
| **`cli.py`**               | **GameController:** Manage overall game flow (Intro, Setup, Battle Loop).                       |
| **`src/actions.py`**       | **HeroActions:** Encapsulate hero’s move logic (Strong, Heal).                                  |
| **`src/battle.py`**        | **BattleManager:** Manage turn-based combat and initiative.                                     |
| **`src/character.py`**     | **OOP Hierarchy:** Base classes (`Character`, `Hero`, `Enemy`) & inheritance.                   |
| **`src/weapon.py`**        | **WeaponFactory:** Create weapon objects with different stats.                                  |
| **`src/setup.py`**         | **GameSetup:** Initialize game environment and entities.                                        |
| **`src/ui/fancy_ui.py`**   | **Facade Pattern:** Combine `DisplayManager`, `MenuManager`, `AnimationManager` for unified UI. |
| **`src/ui/animations.py`** | Manage and display ASCII animations and game banners.                                           |

---

## 🛠️ Technologies

* **Python 3.x**
* **rich:** Powerful library for enhanced terminal UI.

---

## 🤝🏽 Contribution

Feedback, bug reports, or contributions adding new enemies, weapons, or UI features are welcome!

1. Fork the project.
2. Create a new branch (`git checkout -b feature/NewFeature`).
3. Commit your changes (`git commit -m 'feat: Add new enemy type'`).
4. Push your branch (`git push origin feature/NewFeature`).
5. Open a **Pull Request**.

---

## 📃 License

This project is distributed under the [MIT License](LICENSE).

---

## 🙌🏽 Acknowledgments

* Community: A big shoutout to the programming community for providing endless inspiration and support.
* Friends & Peers: For feedback, testing, and encouragement during development.
* Open Source Projects: Thanks to open source games, tutorials, and libraries that inspired and guided this project.

---

*Last updated: Oct 06, 2025*

```
```
